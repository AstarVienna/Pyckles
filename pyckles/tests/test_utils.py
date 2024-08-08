# -*- coding: utf-8 -*-

import pytest
from astropy.io import fits

import pyckles as pyk


@pytest.mark.webtest
class TestGetCatalogList:
    def test_returns_list_of_catalogs_on_server(self):
        cat_list = pyk.get_catalog_list()
        print(cat_list)
        assert "pickles98_full.fits" in cat_list["filename"]


@pytest.mark.webtest
class TestLoadCatalog:
    def test_returns_hdulist_for_correct_catalog_name(self):
        cat = pyk.load_catalog("Pickles")
        assert isinstance(cat, fits.HDUList)
        assert isinstance(cat[6], fits.BinTableHDU)

    def test_throws_if_catalog_name_wrong(self):
        with pytest.raises(ValueError):
            pyk.load_catalog("Bogus")
