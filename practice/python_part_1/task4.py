"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    """
    Calculates the power of each integer and subtracts
    the difference between original previous value and it's power.
    For the first value nothing is subtracted.

    Args:
        ints (List[int]): List of integers.

    Returns:
        List[int]: Power differences of the list of integers.
    """
    # Compute the powers and differences
    powers = [x**2 for x in ints]
    differences = [0] + [x**2 - x for x in ints[:-1]]

    # Create the empty result list
    powers_differences = []

    # Aggregate the power and difference lists into a single tuple list then find power differences
    powers_differences = [power - difference for power, difference in zip(powers, differences)]

    return powers_differences
