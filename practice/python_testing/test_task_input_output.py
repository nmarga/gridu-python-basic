"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
from unittest.mock import patch
from python_part_2.task_input_output import read_numbers

@patch('builtins.input')
def test_read_numbers_without_text_input(mock_input):
    """Test read_numbers function with number input only"""

    mock_input.return_value = '1, 2, 3, 4'
    assert read_numbers(3) == 'Avg: 2.0'

@patch('builtins.input')
def test_read_numbers_with_text_input(mock_input):
    """Test read_numbers function with text input"""

    mock_input.return_value = 'hello, world, foo, bar, baz'
    assert read_numbers(5) == 'No numbers entered'

    mock_input.return_value = '1, 2, hello, 2, world'
    assert read_numbers(5) == 'Avg: 1.67'
