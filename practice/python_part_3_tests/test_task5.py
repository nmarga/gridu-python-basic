"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""
import urllib.error
from unittest.mock import Mock
import pytest
from python_part_3.task5 import make_request

TEST_CASES = [
    ('https://google.com', 200),
    ('https://youtube.com', 200),
]

@pytest.mark.parametrize(['url', 'status'], TEST_CASES)
def test_make_request(url, status):
    """Test make_request function"""

    response_mock = Mock()
    response_mock.read.return_value = (200, 'response_content')

    status_response, _ = make_request(url)
    assert status_response == status

def test_make_request_exception():
    """Test make_request url exceptions"""

    with pytest.raises(urllib.error.URLError):
        make_request('https://non-existent-domain.wxyz')
