"""Scraper definition."""
from typing import Dict
from repository.data_repository import DataRepository
from html_parser.parser import Parser
import requests
import curl_cffi

class Scraper:
    """Scraper class, extracts and processes data from the url."""
    _url: str
    _data_repository: DataRepository
    _headers: Dict

    def __init__(self, url: str, user_agent: str) -> None:
        """Initialize with url, user agent, and stocks count."""
        self._url = url
        self._data_repository = DataRepository()
        self._headers = {
            "User-Agent": user_agent,
        }

    def scrape_profiles(self) -> None:
        """Function to scrape the profile of an active stock."""
        parsed_data = {}
        for tag, _ in self._data_repository.get_stocks().items():
            try:
                print(self._url + f'/quote/{tag}/profile')

                # Impersonate chrome browser to be able to send request
                response = curl_cffi.requests.get(self._url + f'/quote/{tag}/profile',
                                        timeout=3, headers=self._headers, impersonate="chrome")
                html_content = response.text
                print(response.status_code)

            except requests.exceptions.RequestException as e:
                print(f"Error fetching the URL: {e}")
                return
            #print(html_content)
            parsed_data.update(Parser.parse_profile(html_content, tag))

        self._data_repository.insert_profile_data(parsed_data)

    def scrape(self) -> None:
        """Function to scrape most active stocks."""
        try:
            response = requests.get(self._url + '/most-active',
                                    timeout=3, headers=self._headers)
            print(f"Final URL: {response.url}")

            html_content = response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL: {e}")
            return

        parsed_data = Parser.parse_stocks(html_content)

        self._data_repository.insert_stock_data(parsed_data)

    def get_data_lists(self) -> Dict:
        """Method that returns all the processed data."""
        return {"data": self._data_repository.get_profiles()}
