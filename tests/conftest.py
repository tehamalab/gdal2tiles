import shutil
from pathlib import Path

import pytest


@pytest.fixture(scope='function')
def data(tmp_path):
    """A temporary directory containing a copy of the files in data."""
    data_dir = Path('tests/data')

    for data_path in data_dir.iterdir():
        shutil.copy(data_path, tmp_path)

    return tmp_path
