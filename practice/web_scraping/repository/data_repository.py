"""Data repository definition."""
from typing import Dict

class DataRepository:
    """Storage in memory of the scraped data."""
    _stock_data: Dict = {}
    _profile_data: Dict = {}

    def insert_stock_data(self, stock_data: Dict) -> None:
        """Method to add rows the stocks data."""
        self._stock_data.update(stock_data)

    def insert_profile_data(self, profile_data: Dict) -> None:
        """Method to add rows the profile data."""
        self._profile_data.update(profile_data)

    def get_stocks(self) -> Dict:
        """Get all active stocks."""
        return self._stock_data

    def get_profiles(self) -> Dict:
        """Get all stocks profiles."""
        return self._profile_data

    def get_youngest_ceos(self) -> Dict:
        """Get stocks with the youngest CEOs."""
        return self._stock_data
