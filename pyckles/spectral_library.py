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
                warnings.warn(f"Catalogue '{catalog_name}' could not be loaded")

    @property
    def available_spectra(self):
        return self.table["name"]

    def __getattr__(self, item):
        spec = None
        if item in self.table["name"]:
            item_ii = np.where(self.table["name"] == item)[0]
            if len(item_ii) == 1:
                ext = self.table["ext"][item_ii[0]]
                spec = spectrum_from_hdu(self.catalog[ext],
                                         self.meta["return_style"])
            else:
                print(f"Cannot return spectrum for ambiguous name: {item}")
        else:
            raise AttributeError

        return spec

    def __getitem__(self, item):
        return self.__getattr__(item)


def spectrum_from_hdu(hdu, return_type="fits"):
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




