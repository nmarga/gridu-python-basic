import os
import json
from argparse import Namespace
import pytest
from src.processor import DataProcessor
from src.schema import SchemaParser

def test_processor_creates_files(tmp_path):
    args = Namespace(
        path_to_save_files=str(tmp_path),
        files_count=2,
        file_name="testdata",
        file_prefix="count",
        data_lines=5,
        multiprocessing=1,
        data_schema='{"id": "int:1"}'
    )

    processor = DataProcessor(args)
    processor.execute()

    files = os.listdir(tmp_path)
    assert len(files) == 2
    assert any("testdata" in f for f in files)

def test_processor_console_mode(capsys):
    args = Namespace(
        files_count=0,
        data_lines=2,
        data_schema='{"val": "int:10"}',
        path_to_save_files=".",
        multiprocessing=1
    )

    processor = DataProcessor(args)
    processor.execute()

    captured = capsys.readouterr()
    assert '{"val": 10}' in captured.out

def test_processor_file_count_exception():
    args = Namespace(
        files_count=-1,
        data_lines=2,
        data_schema='{"val": "int:10"}',
        path_to_save_files=".",
        multiprocessing = 1
    )

    with pytest.raises(SystemExit):
        processor = DataProcessor(args)
        processor.execute()

@pytest.fixture(name="schema_file_path")
def fixture_schema_file_path(tmp_path):
    d = tmp_path / "subdir"
    d.mkdir()
    schema_file = d / "schema.json"
    schema_file.write_text(json.dumps({"test_key": "int:100"}))
    return str(schema_file)

def test_schema_from_file_fixture(schema_file_path):
    parser = SchemaParser(schema_file_path)
    assert parser.raw_schema["test_key"] == "int:100"

def test_clear_path_action(tmp_path):
    old_file = tmp_path / "0_test_data.json"
    old_file.write_text("old data")

    args = Namespace(
        path_to_save_files=str(tmp_path),
        files_count=1,
        file_name="test_data",
        file_prefix="count",
        data_lines=1,
        multiprocessing=1,
        clear_path=True,
        data_schema='{"a":"int:1"}'
    )

    for f in os.listdir(args.path_to_save_files):
        if f.endswith(f"{args.file_name}.json"):
            os.remove(os.path.join(args.path_to_save_files, f))

    assert len(os.listdir(tmp_path)) == 0

def test_save_to_disk(tmp_path):
    args = Namespace(
        path_to_save_files=str(tmp_path),
        files_count=1,
        file_name="disk_test",
        file_prefix="count",
        data_lines=1,
        multiprocessing=1,
        data_schema='{"a":"int:1"}'
    )
    processor = DataProcessor(args)
    processor.execute()

    expected_file = tmp_path / "disk_test_0_0.json"
    assert expected_file.exists()

def test_multiprocessing_file_count(tmp_path):
    args = Namespace(
        path_to_save_files=str(tmp_path),
        files_count=4,
        file_name="multi",
        file_prefix="count",
        data_lines=1,
        multiprocessing=4,
        data_schema='{"id":"int:rand"}'
    )
    processor = DataProcessor(args)
    processor.execute()

    files = [f for f in os.listdir(tmp_path) if f.endswith(".json")]
    assert len(files) == 4

def test_prefix_uuid_uniqueness(tmp_path):
    args = Namespace(
        path_to_save_files=str(tmp_path),
        files_count=2,
        file_name="unique",
        file_prefix="uuid",
        data_lines=1,
        multiprocessing=1,
        data_schema='{"id":"int:1"}'
    )
    processor = DataProcessor(args)
    processor.execute()

    files = os.listdir(tmp_path)
    assert len(set(files)) == 2
    assert len(files[0]) > 30
