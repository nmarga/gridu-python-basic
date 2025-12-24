"""Scraper definition."""
from typing import Dict
from repository.data_repository import DataRepository
from html_parser.parser import Parser
import requests

class Scraper:
    """Scraper class, extracts and processes data from the url."""
    _url: str
    _count: int
    _data_repository: DataRepository
    _headers: Dict

    def __init__(self, url: str, user_agent: str, count: int) -> None:
        """Initialize with url, user agent, and stocks count."""
        self._url = url
        self._count = count
        self._data_repository = DataRepository()
        self._headers = {
            'User-Agent': user_agent
        }

    def _scrape_profile(self, tag: str) -> None:
        """Function to scrape the profile of an active stock."""
        for profile in self._data_repository.get_stocks():
            try:
                response = requests.get(self._url + f'/quote/{profile[tag]}/profile',
                                        timeout=3, headers=self._headers)
                html_content = response.text
            except requests.exceptions.RequestException as e:
                print(f"Error fetching the URL: {e}")
                return None
        print(html_content)
        parsed_data = Parser.parse_profile(html_content)

        self._data_repository.insert_profile_data(parsed_data)

    def scrape(self) -> None:
        """Function to scrape most active stocks."""
        try:
            response = requests.get(self._url + f'/most-active?count={self._count}',
                                    timeout=3, headers=self._headers)
            html_content = response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the URL: {e}")
            return None

        parsed_data = Parser.parse_stocks(html_content)

        self._data_repository.insert_stock_data(parsed_data)

    def get_data_lists(self) -> Dict:
        """Method that returns all the processed data."""
        return {"data": self._data_repository.get_youngest_ceos(5)}
