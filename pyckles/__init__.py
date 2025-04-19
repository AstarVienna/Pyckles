from .utils import catalogs, load_catalog
from .spectral_library import SpectralLibrary

from importlib import metadata

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    __version__ = "undetermined"
