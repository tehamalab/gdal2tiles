=======
History
=======

0.1.9 (2020-09-30)
------------------

* Enabling GDAL Exceptions.
* Ensuring ``tmscompatible`` option in tile generation and calculation is bool instance.


0.1.8 (2020-09-23)
------------------

* Fix AttributeError ``gdal2tiles.generate_tiles(..., profile='raster', kml=True)``.
  Fix `issue #14 <https://github.com/tehamalab/gdal2tiles/issues/14>`_.


0.1.7 (2020-06-03)
------------------

* Add tile_size option on `generate_tiles` to allow custom tile sizes.
* Small documentation updates.
* Improve basic tests and test against multiple versions of GDAL.


0.1.6 (2020-01-03)
------------------

* Fix some of GDAL installation issues.
* Use pygdal package instead of GDAL dependency.


0.1.5 (2018-08-14)
------------------

* Bug fix.


0.1.4 (2018-08-14)
------------------

* Accept list or tuple in specifying tile generation zoom level.


0.1.3 (2018-07-31)
------------------

* Use billard for multiprocessing if available.


0.1.2 (2018-05-16)
------------------

* Bug fix in ``generate_tiles()``.


0.1.1 (2018-05-10)
------------------

* Clean the source code.
* Setup documentation
* Setup testing environment


0.1.0 (2018-05-06)
------------------

* First release on PyPI.
