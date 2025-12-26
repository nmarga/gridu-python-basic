"""Scraper definition."""
from typing import Dict
from repository.data_repository import DataRepository
from html_parser.parser import Parser
from .request_sender import RequestSender

class Scraper:
    """Scraper class, extracts and processes data from the url."""
    _data_repository: DataRepository
    _request_sender: RequestSender
    def __init__(self, request_sender: RequestSender) -> None:
        """Initialize with url, user agent, and stocks count."""

        self._data_repository = DataRepository()
        self._request_sender = request_sender

    def scrape(self) -> None:
        """Function to scrape most active stocks."""
        html_content = self._request_sender.send_request('/most-active')

        parsed_data = Parser.parse_stocks(html_content)

        self._data_repository.insert_stock_data(parsed_data)

    def scrape_profiles(self) -> None:
        """Function to scrape the profile of an active stock."""
        parsed_data = {}
        for tag, _ in self._data_repository.get_stocks().items():
            html_content = self._request_sender.send_impersonated_request(f'/quote/{tag}/profile')

            parsed_data.update(Parser.parse_profile(html_content, tag))

        self._data_repository.insert_profile_data(parsed_data)

    def scrape_stats(self) -> None:
        """Function to scrape the statistics of an active stock."""
        parsed_data = {}
        for tag, _ in self._data_repository.get_stocks().items():
            url_path = f'/quote/{tag}/key-statistics'
            html_content = self._request_sender.send_impersonated_request(url_path)

            parsed_data.update(Parser.parse_stats(html_content, tag))

        self._data_repository.insert_stats_data(parsed_data)

    def scrape_holders(self) -> None:
        """Function to scrape the holders of an active stock."""
        parsed_data = {}
        for tag, _ in self._data_repository.get_stocks().items():
            html_content = self._request_sender.send_impersonated_request(f'/quote/{tag}/holders')

            parsed_data.update(Parser.parse_holders(html_content, tag))

        self._data_repository.insert_holders_data(parsed_data)

    def get_data_lists(self) -> Dict:
        """Method that returns all the processed data."""
        return {"yongest_ceo_data": self._data_repository.get_youngest_ceos(5),
                "best_changes_data": self._data_repository.get_best_change(10),
                "largest_holds_data": self._data_repository.get_largest_holds(10)}
