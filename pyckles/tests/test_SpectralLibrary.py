import pytest
from astropy.io import fits
from astropy.table import Table

from pyckles import SpectralLibrary


class TestInit:
    def test_initialised_with_nothing(self):
        assert isinstance(SpectralLibrary(), SpectralLibrary)

    def test_initialises_with_correct_name(self):
        pickles = SpectralLibrary("Pickles")
        assert isinstance(pickles, SpectralLibrary)
        assert isinstance(pickles.table, Table)

    def test_nothing_loaded_for_wrong_name(self):
        pickles = SpectralLibrary("Bogus")
        assert isinstance(pickles, SpectralLibrary)
        assert pickles.table is None


class TestGetAttr:
    def test_returns_bintablehdu_for_correct_name_attribute_call(self):
        pickles = SpectralLibrary("Pickles")
        spec = pickles.A0V
        assert isinstance(spec, fits.BinTableHDU)

    def test_returns_attribute_error_if_spec_name_not_in_catalogue(self):
        pickles = SpectralLibrary("Pickles")
        with pytest.raises(AttributeError):
            pickles.ATV

