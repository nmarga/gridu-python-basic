"""
Write a function which divides x by y.
If y == 0 it should print "Division by 0" and return None
elif y == 1 it should raise custom Exception with "Deletion on 1 get the same result" text
else it should return the result of division
In all cases it should print "Division finished"
    >>> division(1, 0)
    Division by 0
    Division finished
    >>> division(1, 1)
    Division finished
    DivisionByOneException("Deletion on 1 get the same result")
    >>> division(2, 2)
    1
    Division finished
"""
from typing import Callable, Union

class DivisionByOneException(Exception):
    """Custom exception for division by one"""

def log_division_result(func: Callable) -> Callable:
    """Decorator for logging the result after the division function call"""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Division finished")
        return result

    return wrapper

@log_division_result
def division(x: int, y: int) -> Union[None, int]:
    """
    Performs division operation.
    Can not divide by 1 or 0.

    Raises:
        DivisionByOneException: This exception is raised when y is equal to 1.
    """

    if y == 1:
        print("Division finished")
        raise DivisionByOneException("Deletion on 1 get the same result")

    try:
        return int(x / y)
    except ZeroDivisionError:
        print("Division by 0")
        return None
