import numpy as np
from astropy.io import ascii, fits
from astropy.utils.data import download_file


SERVER_URL = "https://www.univie.ac.at/simcado/pyckles/"


def get_catalog_list(use_cache=True):
    fname = download_file(SERVER_URL+"index.dat", cache=use_cache)
    return ascii.read(fname)


def load_catalog(cat_name, use_cache=True):
    cat_tbl = get_catalog_list(use_cache=use_cache)

    cat_ii = np.where([cat_name.lower() == cat for cat in cat_tbl["name"]])[0]

    if len(cat_ii) == 0:
        print(f"No catalogues were found containing: {cat_name} \n {cat_tbl}")
        cat = None
    elif len(cat_ii) == 1:
        cat_filename = cat_tbl["filename"][cat_ii[0]]
        cat_path = download_file(SERVER_URL+cat_filename, cache=use_cache)
        cat = fits.open(cat_path)
        cat[0].header["FILENAME"] = cat_path
    elif len(cat_ii) > 1:
        print(f"Ambiguous catalogue name: {cat_name} \n {cat_tbl}")
        cat = None

    return cat
