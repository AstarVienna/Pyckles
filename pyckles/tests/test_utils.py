import pytest
import pyckles as pyk
from astropy.io import fits


class TestGetCatalogList:
    def test_returns_list_of_catalogs_on_server(self):
        cat_list = pyk.get_catalog_list()
        print(cat_list)
        assert "pickles98_full.fits" in cat_list["filename"]


class TestLoadCatalog:
    def test_returns_hdulist_for_correct_catalog_name(self):
        cat = pyk.load_catalog("Pickles")
        assert isinstance(cat, fits.HDUList)
        assert isinstance(cat[6], fits.BinTableHDU)

    def test_returns_none_if_catalog_name_wrong(self):
        cat = pyk.load_catalog("Bogus")
        assert cat is None
