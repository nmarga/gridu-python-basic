import pytest
from src.data_generator import DataGenerator

@pytest.fixture(name="gen")
def fixture_gen() -> DataGenerator:
    return DataGenerator()

def test_get_timestamp(gen: DataGenerator):
    result = gen.get_timestamp(None)
    assert isinstance(result, str)

    assert float(result) > 0

def test_get_str_uuid(gen: DataGenerator):
    result = gen.get_str("rand")

    assert len(result) == 36
    assert "-" in result

def test_get_str_list(gen: DataGenerator):
    options = "['A', 'B', 'C']"
    result = gen.get_str(options)
    assert result in ['A', 'B', 'C']

def test_get_int_range(gen: DataGenerator):
    result = gen.get_int("rand(10, 20)")
    assert 10 <= result <= 20

def test_get_int_list(gen: DataGenerator):
    result = gen.get_int("[-4, 5]")
    assert result in [-4, 5]
