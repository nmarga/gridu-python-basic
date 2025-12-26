"""Data repository definition."""
from typing import Dict

class DataRepository:
    """Storage in memory of the scraped data."""
    _stock_data: Dict = {}
    _profile_data: Dict = {}
    _stats_data: Dict = {}
    _holders_data: Dict = {}

    def insert_stock_data(self, stock_data: Dict) -> None:
        """Method to add rows the stocks data."""
        self._stock_data.update(stock_data)

    def insert_profile_data(self, profile_data: Dict) -> None:
        """Method to add rows the profile data."""
        self._profile_data.update(profile_data)

    def insert_stats_data(self, stats_data: Dict) -> None:
        """Method to add rows the stats data."""
        self._stats_data.update(stats_data)

    def insert_holders_data(self, holder_data: Dict) -> None:
        """Method to add rows the holder data."""
        self._holders_data.update(holder_data)

    def get_stocks(self) -> Dict:
        """Get all active stocks."""
        return self._stock_data

    def get_youngest_ceos(self, limit: int) -> Dict:
        """Get stocks with the youngest CEOs."""
        joined_dict = dict(sorted(
            self._profile_data.items(),
            key=lambda profile:(
                profile[1]['ceo_year_born'] is not None,
                profile[1]['ceo_year_born']),
            reverse=True)[:limit])

        # Join the name
        for key, _ in joined_dict.items():
            joined_dict[key]['name'] = self._stock_data[key]
        return joined_dict

    def get_best_change(self, limit: int) -> Dict:
        """Get stocks with the best 52 week change."""
        joined_dict = dict(sorted(
            self._stats_data.items(),
            key=lambda stat:(
                stat[1]['week_change_52'] is not None,
                stat[1]['week_change_52']),
            reverse=True)[:limit])

        # Join the name
        for key, _ in joined_dict.items():
            joined_dict[key]['name'] = self._stock_data[key]
        return joined_dict

    def get_largest_holds(self, limit: int) -> Dict:
        """Get stocks with the largest holds of Blackrock Inc."""
        joined_dict = dict(sorted(
            self._holders_data.items(),
            key=lambda hold:(
                hold[1]['shares'] is not None,
                hold[1]['shares']),
            reverse=True)[:limit])

        # Join the name
        for key, _ in joined_dict.items():
            joined_dict[key]['name'] = self._stock_data[key]
        return joined_dict
