Welcome to Pyckles's documentation!
===================================

Pyckles is a super simple, light-weight interface to the Pickles (1998)
catalogue of stellar spectra.

.. note:: The package was originally intended only for the Pickles catalogue,
   but it now also has access to the Brown (2014) galaxy spectra catalogue

Which spectra are available
---------------------------

To list which catalogues are available, call ``get_catalog_list``::

   >>> import pyckles
   >>> pyckles.get_catalog_list()
   <Table length=2>
     name    type        filename
     str7    str7         str19
   ------- ------- -------------------
   pickles stellar pickles98_full.fits
     brown  galaxy   brown14_full.fits

To access any of the spectra in the library, we need to create a
``SpectralLibrary`` object using the name of one of the available libraries::

   spec_lib = pyckles.SpectralLibrary("pickles")

To see a list of all the spectra in the catalogue, use the ``available_spectra``
attribute::

   >>> spec_lib.available_spectra

Accessing spectra
-----------------

The spectra can be accessed both as items and as attributes of the
``SpectralLibrary``.

As an item::

   >>> a0v = spec_lib["A0V"]

or as an attribute::

   >>> a0v = spec_lib.A0V

.. note:: If there there is a space in the name, the attribute call will not work

Spectra are returned as ``astropy.fits.BinTableHDU`` objects, and so the
wavelength and flux information is contained in the ``.data`` attrribute of the
returned object::

   >>> from matplotlib import pyplot as plt
   >>> plt.plot(spec_lib.A0V.data["wavelength"],
                spec_lib.A0V.data["flux"])
   >>> plt.plot(spec_lib["G2V"].data["wavelength"],
                spec_lib.["G2V"].data["flux"])

Alternatively, if we have ``synphot`` installed, we can set tell the
``SpectralLibrary`` to return the spectra as ``synphot.SourceSpectrum`` objects
by setting the ``.meta["return_style"]`` property to ``synphot``::

   >>> spec_lib.meta["return_style"] = "synphot"      # default is "fits"


Adding libraries
----------------

If you have a spectral library that you would like added to ``pyckles``, please
open an issue on github and we can talk about about adding in.

Library file formatting
+++++++++++++++++++++++

Libraries are stored in a single FITS files with a contents table in the first
extension, and the spectra in further BinTableHDU extensions

========= =========== ========
Extension HDU type    Contents
--------- ----------- --------
0         PrimaryHDU
1         BinTableHDU Index table mapping spectra to extensions
[1+n]     BinTableHDU [n additional tables of spectra indexes]
X         BinTableHDU First of m spectra
X+m       BinTableHDU m-th spectra
========= =========== ========

Index table extensions
++++++++++++++++++++++

The first extension should contain a table with (at a minimum) the following
columns:

========= ====
extension name
--------- ----
X         A0V
X+1       A0III
...
X+m       M9V
========= ====

Additional spectra index tables can be included, but this means that all index
tables must be updated to keep the extension column pointing to the correct
spectra. For example in the pickles library, ``ext 1`` indexes all the spectra
contained in the original Pickles (1998) library, however for ease of use, I
have added a further extension index in ``ext 2`` which only includes the main
sequence stars. Additionally ``ext 3`` contains a table with physical properties
of each of the spectral types, such as temperature and evolutionary stage. The
actual spectra are only contained onwards from ``ext 4``.

Spectra extensions
++++++++++++++++++

The spectra are simple BinTableHDU objects containing 2 columns: ``wavelength``
and ``flux``.

========== ====
wavelength flux
---------- ----
...        ...
========== ====

If ``astropy`` is used to create these tables the headers will be
taken care of. If not, the following header information should be included::

    TTYPE1  = 'wavelength'
    TFORM1  = 'D       '
    TUNIT1  = 'Angstrom'
    TTYPE2  = 'flux    '
    TFORM2  = 'D       '
    TUNIT2  = 'Angstrom-1 cm-1 erg s-1'

where the ``TUNITn`` keywords are in readable by ``astropy.units``.



.. toctree::
   :maxdepth: 2
   :caption: Contents:

