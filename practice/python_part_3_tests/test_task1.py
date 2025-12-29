"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""
from datetime import datetime
import time
import pytest
from python_part_3.task1 import calculate_days, WrongFormatException

@pytest.mark.freeze_time('2025-12-08')
def test_calculate_days():
    """Test calculate_days function"""

    # Check that the time is frozen in tests
    now = datetime.now()
    time.sleep(1)
    later = datetime.now()
    assert now == later

    assert calculate_days('2025-12-08') == 0
    assert calculate_days('2025-12-31') == -23
    assert calculate_days('2025-12-01') == 7


@pytest.mark.freeze_time('2025-12-08')
def test_calculate_days_exception():
    """Test calculate_days function exceptions"""

    with pytest.raises(WrongFormatException):
        calculate_days('25-12-08')

    with pytest.raises(WrongFormatException):
        calculate_days('2025-12-32')

    with pytest.raises(WrongFormatException):
        calculate_days('2025-13-08')
