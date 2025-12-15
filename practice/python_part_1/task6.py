"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    """
    Reads the file line by line and calculates the minimum and maximum value.

    Args:
        filename (str): The relative path filename.

    Returns:
        Tuple[int, int]: A tuple with minimum and maximum value.
    """

    # Create the list to store the integers
    ints = []

    # Read the file in read mode
    with open(filename, 'r') as opened_file:
        for line in opened_file:
            # Append the parsed to integer line
            ints.append(int(line))

    # Return the min and max tuple
    return (min(ints), max(ints))
