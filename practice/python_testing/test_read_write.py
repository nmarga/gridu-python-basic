"""
Write tests for 2_python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import pytest
from python_part_2.task_read_write import read_files

FILE_CASES = [
    ('file1.txt', '80'),
    ('file2.txt', '37'),
    ('file3.txt', '15'),
    ('file4.txt', '-15'),
]

OUTPUT_FILE = ('result.txt', '80, 37, 15, -15')

@pytest.mark.parametrize(['filename', 'value'], FILE_CASES)
def test_create_file(filename: str, value: int, tmp_path):
    """Test the creation of a single file in a temp path"""

    f = tmp_path / filename
    f.write_text(str(value))

    # Read the value from the created file
    assert f.read_text() == value

    # Check if there is a single file only created
    assert len(list(tmp_path.glob('*'))) == 1

@pytest.mark.parametrize(['filename', 'value'], FILE_CASES)
def test_create_files_in_dir(filename: str, value: int, custom_temp_dir):
    """Test the creation of multiple files in a temp path"""

    f = custom_temp_dir / filename
    f.write_text(str(value))

    # Read the value from the created file
    assert f.read_text() == value

def test_check_file_count_in_dir(custom_temp_dir):
    """Test the count of the created files in the temp path"""

    # Check that the amount of files matches the FILE_CASES
    assert len(list(custom_temp_dir.glob('*'))) == len(FILE_CASES)

def test_read_files_function(custom_temp_dir):
    """Test the read_files function on the temp path"""

    read_files(str(custom_temp_dir))

    output_filename, contents = OUTPUT_FILE
    output_file = custom_temp_dir.parent / output_filename

    assert output_file.exists()
    assert output_file.read_text() == contents
