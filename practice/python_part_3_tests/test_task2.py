"""
Write tests for math_calculate function
"""
from python_part_3.task2 import math_calculate, OperationNotFoundException
import pytest

def test_math_calculate():
    """Some tests for math_calculate function"""

    assert math_calculate('log', 1024, 2) == 10.0
    assert math_calculate('ceil', 10.7) == 11
    assert round(math_calculate('sqrt', 3), 2) == 1.73

def test_math_calculate_exceptions():
    """Some tests for math_calculate exceptions"""

    with pytest.raises(OperationNotFoundException):
        math_calculate('test', 1, 2)

    with pytest.raises(TypeError):
        math_calculate('sqrt', 1, 2)
    with pytest.raises(TypeError):
        math_calculate('pi')
