import warnings
import numpy as np
from astropy.table import Table

from .core import load_catalog


class SpectralLibrary:
    def __init__(self, catalog_name=None, **kwargs):

        self.catalog_name = catalog_name
        self.catalog = None
        self.table = None

        self.meta = {"use_cache": True}
        self.meta.update(kwargs)

        self.load(catalog_name)

    def load(self, catalog_name):
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
                spec = self.catalog[ext]
            else:
                print(f"Cannot return spectrum for ambiguous name: {item}")
        else:
            raise AttributeError

        return spec

    def __getitem__(self, item):
        return self.__getattr__(item)
