"""
Write a parametrized test for two functions.
The functions are used to find a number by ordinal in the Fibonacci sequence.
One of them has a bug.

Fibonacci sequence: https://en.wikipedia.org/wiki/Fibonacci_number

Task:
 1. Write a test with @pytest.mark.parametrize decorator.
 2. Find the buggy function and fix it.
"""
import pytest

def fibonacci_1(n: int) -> int:
    if n == 0:
        return 0
    if n < 0:
        raise ValueError("Can not compute fibonacci number for index smaller than 0")

    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b


def fibonacci_2(n: int) -> int:
    if n == 0:
        return 0
    if n < 0:
        raise ValueError("Can not compute fibonacci number for index smaller than 0")

    fibo = [0, 1]
    for i in range(1, n+1):
        # The fix is that it should be i and i - 1 not i - 1 and i - 2
        fibo.append(fibo[i] + fibo[i-1])
    return fibo[n]

TEST_CASES = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (7, 13),
    (11, 89),
    (24, 46368),
]

@pytest.mark.parametrize(['n', 'fib_n'], TEST_CASES)
def test_fibonacci(n, fib_n):
    """Test fibonacci methods"""

    assert fibonacci_1(n) == fib_n
    assert fibonacci_2(n) == fib_n

def test_fibonacci_exception():
    """Test fibonacci with exceptions"""

    with pytest.raises(ValueError):
        fibonacci_1(-2)

    with pytest.raises(ValueError):
        fibonacci_2(-2)
