"""
write tests for is_http_domain function
"""
from python_part_3.task3 import is_http_domain
import pytest

TEST_CASES = [
    ('https://example.com', True),
    ('https://my-app.test', True),
    ('https://subdomain-example.example.org', True),
    ('http://example.com.', False),
    ('http://api.example.com/', True),
    ('http://api-.example.com/', False),
    ('http://api-.example.com/', False),
    ('https://subdomain--example.example.org/', False),
    ('https://staging.api.example.com', True),
    ('ftp://example.com', False),
    ('https:/example.com', False),
    ('https://example..com', False),
    ('example.com', False),
    ('HTTPS://Example.COM', True),
    ('http://192.0.2.1', True),
    ('https://example.com.' + 'test'*16, False),
]


@pytest.mark.parametrize(['domain', 'result'], TEST_CASES)
def test_is_http_domain(domain: str, result: bool):
    """Test the is_http_domain function"""

    assert is_http_domain(domain) == result
