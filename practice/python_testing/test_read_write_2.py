"""
Write tests for 2_python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import re
import pytest
from python_part_2.task_read_write_2 import generate_words, write_random_words

def test_generate_words_lengths():
    """Test the generation of word lengths from the generate_words function"""

    # Test word count
    assert len(generate_words()) == 20
    assert len(generate_words(10)) == 10
    assert len(generate_words(3)) == 3

    # Test some edge cases
    assert len(generate_words(-10)) == 0

    with pytest.raises(TypeError):
        len(generate_words('ignored_type')) # type: ignore
    with pytest.raises(TypeError):
        len(generate_words(34.33)) # type: ignore

    # Test character number bounds
    for word in generate_words():
        assert 3 <= len(word) <= 10

def test_generate_words_character_type():
    """Test the generation of word regex pattern"""

    for word in generate_words():
        assert re.fullmatch(r'[a-z]+', word)

def test_write_random_words(custom_temp_dir, mocker):
    """Test the write_random_words function"""
    write_random_words(word_count=15, dir_path=str(custom_temp_dir))

    file1 = custom_temp_dir / "file1.txt"
    file2 = custom_temp_dir / "file2.txt"

    assert file1.exists()
    assert file2.exists()

    assert len(file1.read_text().split('\n')) == 15
    assert len(file2.read_text().split(', ')) == 15
# @pytest.mark.parametrize(['filename', 'value'], FILE_CASES)
# def test_create_files_in_dir(filename: str, value: int, custom_temp_dir):
#     """Test the creation of multiple files in a temp path"""

#     f = custom_temp_dir / filename
#     f.write_text(str(value))

#     # Read the value from the created file
#     assert f.read_text() == value

# def test_check_file_count_in_dir(custom_temp_dir):
#     """Test the count of the created files in the temp path"""

#     print(custom_temp_dir)

#     # Check that the amount of files matches the FILE_CASES
#     assert len(list(custom_temp_dir.glob('*'))) == len(FILE_CASES)
