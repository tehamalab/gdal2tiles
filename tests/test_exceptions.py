import pytest

from gdal2tiles import generate_tiles


def test_gdal_useexceptions():
    """Ensure GDAL raises Exceptions instead of Error values"""
    with pytest.raises(RuntimeError):
        generate_tiles('/dummy/file.tiff', '/tmp/gdal2tiles/tests/dummy')
