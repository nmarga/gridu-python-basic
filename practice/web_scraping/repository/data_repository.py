"""Data repository definition"""
from typing import List

class DataRepository:
    """Storage in memory of the scraped data"""
    _data: List = []

    def set_data(self, data: List):
        """Method to set the data"""
        self._data = data

    def get_youngest_ceos(self, limit: int) -> List:
        """Get stocks with the youngest CEOs"""
        return self._data
