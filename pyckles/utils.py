# -*- coding: utf-8 -*-
"""Utility functions."""

from astropy.io import fits, ascii as ascii_io
from astropy.utils.data import download_file


SERVER_URL = "https://scopesim.univie.ac.at/pyckles/"


def get_catalog_list(use_cache=True):
    """
    Return a list of catalogues based on the server index file.

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
    catalogs = ascii_io.read(fname)
    catalogs.add_index("name", unique=True)
    return catalogs


def load_catalog(cat_name, use_cache=True):
    """
    Load a catalogue file into memory.

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

    try:
        cat_filename = cat_tbl.loc[cat_name.lower()]["filename"]
    except KeyError as err:
        raise ValueError(
            f"No catalogues were found containing: '{cat_name}' \n {cat_tbl}"
        ) from err

    # unique in index should take care of potential duplicates, however check
    assert isinstance(cat_filename, str), "Duplicates in cat name."

    cat_path = download_file(SERVER_URL+cat_filename, cache=use_cache)

    # TODO: should use context manager for file open...
    cat = fits.open(cat_path)
    cat[0].header["FILENAME"] = cat_path  # pylint: disable=maybe-no-member

    return cat
