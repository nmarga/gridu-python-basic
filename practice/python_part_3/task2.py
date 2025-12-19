"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import math
from typing import Any

class OperationNotFoundException(Exception):
    """Custom exception for operation not found."""

def math_calculate(function: str, *args) -> Any:
    """Executes custom operation from math module."""

    expression = 'math.' + function + '(' + ', '.join([str(operand) for operand in args]) + ')'
    try:
        return eval(expression)
    except AttributeError as e:
        raise OperationNotFoundException(e) from e
