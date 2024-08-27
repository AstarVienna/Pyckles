# -*- coding: utf-8 -*-
"""Utility functions."""

from pathlib import Path

from astropy.io import fits
from astropy.table import Table

import pooch


catalogs = Table.read(Path(__file__).parent / "index.dat", format="ascii")
catalogs.add_index("name", unique=True)


retriever = pooch.create(
    path=(Path.home() / ".astar/pyckles"),
    base_url="https://scopesim.univie.ac.at/pyckles/",
    registry=dict(catalogs[["filename", "hash"]].iterrows()),
    retry_if_failed=3,
    # The name of an environment variable that can overwrite the path
    env="ASTAR_CACHE_DIR",
)


def load_catalog(cat_name):
    """
    Load a catalogue file into memory.

    Parameters
    ----------
    cat_name : str
        A valid catalogue name

    Returns
    -------
    cat : astropy.fits.HDUList
        A handle to an astropy FITS object containing all the spectra and index
        information

    """
    try:
        cat_filename = catalogs.loc[cat_name.lower()]["filename"]
    except KeyError as err:
        raise ValueError(
            f"No catalogues were found containing: '{cat_name}' \n"
            f"Available catalogs:\n{catalogs[['name', 'type']]}"
        ) from err

    # unique in index should take care of potential duplicates, however check
    assert isinstance(cat_filename, str), "Duplicates in cat name."

    cat_path = retriever.fetch(cat_filename)

    # TODO: should use context manager for file open...
    cat = fits.open(cat_path)
    cat[0].header["FILENAME"] = cat_path  # pylint: disable=maybe-no-member

    return cat
