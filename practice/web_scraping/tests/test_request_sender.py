import os
from dotenv import load_dotenv
import pytest
from scraper.request_sender import RequestSender

@pytest.fixture(name="request_sender_connection")
def fixture_request_sender_connection():
    """Fixture for the RequestSender object."""
    load_dotenv()
    yield RequestSender(os.getenv("TARGET_URL", ""),
                         os.getenv("USER_AGENT", ""))

def test_connection_response(request_sender_connection):
    """Function to test the response of the pages."""
    _, status_code = request_sender_connection.send_request('/most-active')
    assert status_code == 200
    _, status_code = request_sender_connection.send_impersonated_request('/most-active')
    assert status_code == 200

def test_connection_response_exception(request_sender_connection):
    """Function to test error response of the pages."""
    _, status_code = request_sender_connection.send_request(
        '/non-existent-not-found-page')
    assert status_code == 404
    _, status_code = request_sender_connection.send_impersonated_request(
        '/non-existent-not-found-page')
    assert status_code == 404
