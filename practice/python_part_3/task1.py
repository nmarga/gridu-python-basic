"""
using datetime module find number of days from custom date to now
Custom date is a string with format "2021-12-24"
If entered string pattern does not match, raise a custom Exception
If entered date is from future, return negative value for number of days
    >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
    -1
    >>> calculate_days('2021-10-05')
    1
    >>> calculate_days('10-07-2021')
    WrongFormatException
"""
from datetime import datetime

class WrongFormatException(Exception):
    """Wrong format exception error"""

def calculate_days(from_date: str) -> int:
    """Finds the number of days from custom date to now"""

    try:
        delta_time = datetime.now() - datetime.fromisoformat(from_date)
    except ValueError as e:
        raise WrongFormatException(e) from e

    return delta_time.days
