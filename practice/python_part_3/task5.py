"""
Write a function that makes a request to some url
using urllib. Return status code and decoded response data in utf-8
Examples:
     >>> make_request('https://www.google.com')
     200, 'response data'
"""
from typing import Tuple
import urllib.request
import ssl
import certifi

def make_request(url: str) -> Tuple[int, str]:
    """
    Makes a request to an url.

    Args:
        url (str): Url string.

    Returns:
        Tuple[int, str]: A tuple that contains the response status, and response data.
    """

    ssl_context = ssl.create_default_context(cafile=certifi.where())

    with urllib.request.urlopen(url, context=ssl_context) as response:
        data = response.read()
        try:
            return (response.status, data.decode('UTF-8'))
        except UnicodeDecodeError:
            return (response.status, data)
