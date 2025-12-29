"""Config for test"""
import pytest


@pytest.fixture(scope="module")
def custom_temp_dir(tmp_path_factory):
    """Fixture for a text file that persists through the module runtime"""
    dir_path = tmp_path_factory.mktemp("data_dir")
    return dir_path
