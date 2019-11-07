import numpy as np
from astropy.io import ascii, fits
from astropy.utils.data import download_file


SERVER_URL = "https://www.univie.ac.at/simcado/pyckles/"


def get_catalog_list(use_cache=True):
    """
    Returns a list of catalogues based on the server index file

    Parameters
    ----------
    use_cache : bool
        Read a local copy (True) or get the list from the server (False)

    Returns
    -------
    catalogs : astropy.Table
        A table with information about the available catalogues

    """
    fname = download_file(SERVER_URL+"index.dat", cache=use_cache)
    catalogs = ascii.read(fname)
    return catalogs


def load_catalog(cat_name, use_cache=True):
    """
    Loads a catalogue file into memory

    If ``use_cache=True`` a local copy of the catalogue FITS file is loaded,
    otherwise the catalogue is downloaded from the server.

    To refresh the local copy of the catalogue file, call the ``astropy``
    function ``astropy.utils.data.clear_download_cache()``

    Parameters
    ----------
    cat_name : str
        A valid catalogue name

    use_cache : bool
        Default is True. If False, the catalogue file is fetched from the server

    Returns
    -------
    cat : astropy.fits.HDUList
        A handle to an astropy FITS object containing all the spectra and index
        information

    """
    cat_tbl = get_catalog_list(use_cache=use_cache)

    cat_ii = np.where([cat_name.lower() == cat for cat in cat_tbl["name"]])[0]

    if len(cat_ii) == 0:
        print("No catalogues were found containing: {} \n {}"
              "".format(cat_name, cat_tbl))
        cat = None
    elif len(cat_ii) == 1:
        cat_filename = cat_tbl["filename"][cat_ii[0]]
        cat_path = download_file(SERVER_URL+cat_filename, cache=use_cache)
        cat = fits.open(cat_path)
        cat[0].header["FILENAME"] = cat_path
    elif len(cat_ii) > 1:
        print("Ambiguous catalogue name: {} \n {}"
              "".format(cat_name, cat_tbl))
        cat = None

    return cat
