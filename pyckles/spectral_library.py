import warnings
import numpy as np
from astropy.table import Table
from astropy import units as u

from .utils import load_catalog


class SpectralLibrary:
    """
    A container for a library of spectra

    Holds and returns spectra from various catalogues in various python-friendly
    formats, such as: ``synphot.SourceSpectrum``, ``astropy.Quantity``,
    ``numpy.ndarray``, and ``fits.BinTableHDU``

    Spectra can be accessed by using the attribute syntax::

        >>> spec_lib = pyckles.SpectralLibrary("pickles")
        >>> spec_lib.A0V

    or using the item syntax::

        >>> spec_lib["A0V"]

    The returned spectrum is formatted according to the ``meta["return_style"]``
    parameter::

        >>> spec_lib.meta["return_style"] = 'fits'
        >>> type(spec_lib.A0V)
        astropy.io.fits.hdu.table.BinTableHDU


    Parameters
    ----------
    catalog_name : str
        The name of the spectral catalogue. See ``get_catalog_list``

    Keyword arguments
    -----------------
    use_cache : bool
        Default is True. If False, re-downloads the catalogue from the server
        Note: if you need to update the catalogue just once, call
        ``astropy.utils.data.clear_download_cache()``

    return_style : str
        - ``fits``: Returns the original FITS BinTableHDU object
        - ``synphot``: Returns a ``synphot.SourceSpectrum`` object
        - ``quantity``: Returns wavelength and flux as ``astropy.Quantity``
        - ``array``: Returns wavelength and flux as ``numpy.ndarray``

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

        self.meta = {"use_cache": True,
                     "return_style": "fits"}
        self.meta.update(kwargs)

        self.load(catalog_name)

    def load(self, catalog_name):
        """ Loads the catalogue for a valid string ``catalog_name`` """
        if catalog_name is not None:
            self.catalog = load_catalog(catalog_name, self.meta["use_cache"])
            if self.catalog is not None:
                self.table = Table(self.catalog[1].data)
            else:
                warnings.warn("Catalogue '{}' could not be loaded"
                              "".format(catalog_name))

    @property
    def available_spectra(self):
        return self.table["name"]

    def __getattr__(self, item):
        """Looks for item in the 'name' column of self.table"""
        spec = None
        if item in self.table["name"]:
            item_ii = np.where(self.table["name"] == item)[0]
            if len(item_ii) == 1:
                ext = self.table["ext"][item_ii[0]]
                spec = spectrum_from_hdu(self.catalog[ext],
                                         self.meta["return_style"])
            else:
                print("Cannot return spectrum for ambiguous name: {}"
                      "".format(item))
        else:
            raise AttributeError

        return spec

    def __getitem__(self, item):
        return self.__getattr__(item)


def spectrum_from_hdu(hdu, return_type="fits"):
    """
    Converts a BinTableHDU into the required return_type format

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
        spec = [wave << wave_unit, flux << flux_unit]
    elif return_type.lower() == "array":
        spec = [wave, flux]
    elif return_type.lower() == "synphot":
        from synphot import Empirical1D, SourceSpectrum
        spec = SourceSpectrum(Empirical1D,
                              points=wave << wave_unit,
                              lookup_table=flux << flux_unit)
    else:
        spec = hdu

    return spec




