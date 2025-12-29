"""
Write tests for division() function in 2_python_part_2/task_exceptions.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""
import pytest
from python_part_2.task_exceptions import division, DivisionByOneException

TEST_CASES = [
    (2, 3, 0),
    (100, 10, 10),
    (0, 5, 0),
    (99, 2, 49),
]

@pytest.mark.parametrize(['a', 'b', 'c'], TEST_CASES)
def test_division_ok(a: int, b: int, c: int, capfd):
    """Test the output of division when there are no exceptions"""

    assert division(a, b) == c

    captured = capfd.readouterr()
    assert "Division finished\n" in captured.out

def test_division_by_zero(capfd):
    """Test the output of division by 0"""

    assert division(5, 0) is None

    captured = capfd.readouterr()
    assert "Division by 0\n" in captured.out
    assert "Division finished\n" in captured.out

def test_division_by_one(capfd):
    """Test the output of division by 1"""

    with pytest.raises(DivisionByOneException):
        division(5, 1)

    captured = capfd.readouterr()
    assert "Division finished\n" in captured.out
