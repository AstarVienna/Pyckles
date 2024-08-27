# -*- coding: utf-8 -*-
"""Main module."""

from astropy.table import Table
from astropy import units as u

from .utils import load_catalog


class SpectralLibrary:
    """
    A container for a library of spectra.

    Holds and returns spectra from various catalogues in various
    "python-friendly" formats, such as: ``synphot.SourceSpectrum``,
    ``astropy.Quantity``, ``numpy.ndarray``, and ``fits.BinTableHDU``

    Spectra can be accessed by using the attribute syntax::

        >>> spec_lib = pyckles.SpectralLibrary("pickles")
        >>> spec_lib.A0V

    or using the item syntax::

        >>> spec_lib["A0V"]

    The returned spectrum is formatted according to ``meta["return_style"]``
    parameter::

        >>> spec_lib.meta["return_style"] = 'fits'
        >>> type(spec_lib.A0V)
        astropy.io.fits.hdu.table.BinTableHDU


    Parameters
    ----------
    catalog_name : str
        The name of the spectral catalogue. See ``pyckles.catalogs``

    Keyword arguments
    -----------------
    return_style : str
        - "fits": Returns the original FITS BinTableHDU object
        - "synphot": Returns a ``synphot.SourceSpectrum`` object
        - "quantity": Returns wavelength and flux as ``astropy.Quantity``
        - "array": Returns wavelength and flux as ``numpy.ndarray``

    Examples
    --------
    List the available spectra::

        >>> import pyckles
        >>> spec_lib = pyckles.SpectralLibrary("pickles", return_style="quantity")
        >>> spec_lib.available_spectra
        <Column name='name' dtype='str5' length=131>
          A0I
        A0III
         A0IV
          ...
        K2III
        K3III
        K4III

    Get an A0V spectrum::

        >>> vega = spec_lib.A0V
        >>> vega
        [<Quantity [ 1150.,  1155.,  1160., ..., 24990., 24995., 25000.] Angstrom>,
        <Quantity [0.181751, 0.203323, 0.142062, ..., 0.00699 , 0.006986, 0.006983] erg / (Angstrom cm2 s)>]

    Return synphot.SourceSpectrum objects instead of a list of Quantity arrays::

        >>> spec_lib.meta["return_style"] = "synphot"
        >>> spec_lib.A0V
        <synphot.spectrum.SourceSpectrum at 0x251800272e8>

    """

    def __init__(self, catalog_name=None, **kwargs):
        self.catalog_name = catalog_name
        self.catalog = None
        self.table = None

        self.meta = {"return_style": "fits"} | kwargs
        self.load(catalog_name)

    def load(self, catalog_name):
        """Load the catalogue for a valid string ``catalog_name``."""
        if catalog_name is None:
            return  # TODO: is this really wise?

        self.catalog = load_catalog(catalog_name)
        # pylint: disable=maybe-no-member
        self.table = Table(self.catalog[1].data)
        self.table["name"] = [name.strip() for name in self.table["name"]]
        self.table.add_index("name", unique=True)

    @property
    def available_spectra(self):
        """Return table column containing all spectra name in the library."""
        return self.table["name"]

    def __getattr__(self, item):
        """Look for `item` in the 'name' column of `self.table`."""
        try:
            ext = int(self.table.loc[item]["ext"])
        except KeyError as err:
            raise ValueError(f"No spectrum found for name '{item}'") from err

        spec = spectrum_from_hdu(self.catalog[ext], self.meta["return_style"])
        return spec

    def __getitem__(self, item):
        """Forward to __getattr__."""
        return self.__getattr__(item)


def spectrum_from_hdu(hdu, return_type="fits"):
    """
    Convert a ``BinTableHDU`` into the required `return_type` format.

    Parameters
    ----------
    hdu : BinTableHDU
        A BinTableHDU spectrum with column names: ``wavelength``, ``flux``

    return_type : str
        The format of the returned spectra - See SpectralLibrary docs

    Returns
    -------
    spec : various
        See above

    See Also
    --------
    SpectralLibrary

    """
    wave = hdu.data["wavelength"]
    flux = hdu.data["flux"]
    wave_unit = u.Unit(hdu.header["TUNIT1"])
    flux_unit = u.Unit(hdu.header["TUNIT2"])

    if return_type.lower() == "quantity":
        return wave << wave_unit, flux << flux_unit

    if return_type.lower() == "array":
        return wave, flux

    if return_type.lower() == "synphot":
        # Import here because synphot is an extra (optional) dependency
        from synphot import Empirical1D, SourceSpectrum
        spec = SourceSpectrum(
            Empirical1D,
            points=(wave << wave_unit),
            lookup_table=(flux << flux_unit)
        )
    else:
        spec = hdu

    return spec
