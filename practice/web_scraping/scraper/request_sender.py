"""RequestSender class definition with cached methods."""
from typing import Dict
from datetime import timedelta
import requests
import curl_cffi
from cachier import cachier

class RequestSender:
    """RequestSender class, it sends requests to url paths from a base url specification."""
    _base_url: str
    _headers: Dict

    def __init__(self, url: str, user_agent: str) -> None:
        """Initialize with url, user agent, and stocks count."""
        self._base_url = url
        self._headers = {
            "User-Agent": user_agent,
        }

    @cachier(stale_after=timedelta(hours=12))
    def send_request(self, url_path):
        """Send standard simple requests.get request"""
        response = requests.get(self._base_url + url_path,
                                timeout=3, headers=self._headers)
        return response.text

    @cachier(stale_after=timedelta(hours=12))
    def send_impersonated_request(self, url_path):
        """Impersonate chrome browser to be able to send request"""
        response = curl_cffi.requests.get(self._base_url + url_path,
                                          timeout=10, headers=self._headers, impersonate="chrome")
        return response.text
