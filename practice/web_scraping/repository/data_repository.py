"""Data repository definition."""
from typing import List

class DataRepository:
    """Storage in memory of the scraped data."""
    _stock_data: List = []
    _profile_data: List = []

    def insert_stock_data(self, stock_data: List) -> None:
        """Method to add rows the stocks data."""
        self._stock_data += stock_data

    def insert_profile_data(self, profile_data: List) -> None:
        """Method to add rows the profile data."""
        self._stock_data += profile_data

    def get_stocks(self) -> List:
        """Get all active stocks."""
        return self._stock_data

    def get_profiles(self) -> List:
        """Get all stocks profiles."""
        return self._profile_data

    def get_youngest_ceos(self, limit: int) -> List:
        """Get stocks with the youngest CEOs."""
        return self._stock_data
