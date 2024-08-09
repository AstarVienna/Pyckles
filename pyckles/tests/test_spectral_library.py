# -*- coding: utf-8 -*-

import pytest
import numpy as np
from astropy.io import fits
from astropy.table import Table, Column
from astropy import units as u
from synphot import SourceSpectrum

from pyckles import SpectralLibrary


class TestInit:
    def test_initialised_with_nothing(self):
        assert isinstance(SpectralLibrary(), SpectralLibrary)

    @pytest.mark.webtest
    def test_initialises_with_correct_name(self):
        pickles = SpectralLibrary("Pickles")
        assert isinstance(pickles, SpectralLibrary)
        assert isinstance(pickles.table, Table)
        assert isinstance(pickles.available_spectra, Column)

    @pytest.mark.webtest
    def test_throws_for_wrong_name(self):
        with pytest.raises(ValueError):
            SpectralLibrary("Bogus")


@pytest.mark.webtest
class TestGetAttr:
    def test_returns_bintablehdu_for_correct_name_attribute_call(self):
        pickles = SpectralLibrary("Pickles")
        spec = pickles.A0V
        assert isinstance(spec, fits.BinTableHDU)

    def test_throws_if_spec_name_not_in_catalogue(self):
        pickles = SpectralLibrary("Pickles")
        with pytest.raises(ValueError):
            pickles.ATV

    def test_returns_arrays_with_return_style_set_to_array(self):
        pickles = SpectralLibrary("Pickles")
        pickles.meta["return_style"] = "array"
        spec = pickles.A0V
        assert isinstance(spec[0], np.ndarray)
        assert isinstance(spec[1], np.ndarray)

    def test_returns_quantity_with_return_style_set_to_quantity(self):
        pickles = SpectralLibrary("Pickles")
        pickles.meta["return_style"] = "quantity"
        spec = pickles.A0V
        assert isinstance(spec[1], u.Quantity)
        assert spec[1].unit == u.Unit("erg s-1 angstrom-1 cm-2")

    def test_returns_sourcespectrum_with_return_style_set_to_synphot(self):
        pickles = SpectralLibrary("Pickles")
        pickles.meta["return_style"] = "synphot"
        spec = pickles.A0V
        assert isinstance(spec, SourceSpectrum)

    def test_also_works_for_getitem(self):
        pickles = SpectralLibrary("Pickles")
        spec = pickles["A0V"]
        assert isinstance(spec, fits.BinTableHDU)

    def test_throws_for_invalid_library_name(self):
        with pytest.raises(ValueError):
            SpectralLibrary("bogus")


@pytest.mark.webtest
def test_strips_whitespace():
    pickles = SpectralLibrary("Pickles")
    assert "M25V" in pickles.available_spectra
    assert "M25V   " not in pickles.available_spectra
