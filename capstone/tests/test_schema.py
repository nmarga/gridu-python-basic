import json
import pytest
from src.schema import SchemaParser
from src.data_generator import DataGenerator


@pytest.fixture(name="parser")
def fixture_parser(tmp_path) -> SchemaParser:
    schema_file = tmp_path / "schema.json"
    schema_file.write_text(json.dumps({"age": "int:rand(1,5)", "name": "str:rand"}))
    return SchemaParser(str(schema_file))

def test_generate_line_structure(parser: SchemaParser):
    line = parser.generate_line()
    assert "age" in line
    assert "name" in line
    assert 1 <= int(line["age"]) <= 5

def test_invalid_json_exits(tmp_path):
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("{ invalid json }")
    with pytest.raises(SystemExit):
        SchemaParser(str(bad_file))

DATA_TYPE_TEST_CASES = [
    ("int", "rand(1, 10)", int),
    ("str", "rand", str),
    ("int", "[1, 2, 3]", int),
    ("str", "['a', 'b']", str)
]

@pytest.mark.parametrize("dtype, instruction, expected_type", DATA_TYPE_TEST_CASES)
def test_data_types(dtype, instruction, expected_type):
    gen = DataGenerator()
    if dtype == "int":
        result = gen.get_int(instruction)
    else:
        result = gen.get_str(instruction)
    assert isinstance(result, expected_type)

SCHEMA_TEST_CASES = [
    '{"id": "int:rand", "name": "str:rand"}',
    '{"age": "int:[20, 30]", "status": "str:[\'active\']"}',
    '{"timestamp": "timestamp:"}'
]

@pytest.mark.parametrize("schema_str", SCHEMA_TEST_CASES)
def test_different_schemas(schema_str):
    parser = SchemaParser(schema_str)
    line = parser.generate_line()
    assert isinstance(line, dict)
    assert len(line) > 0
