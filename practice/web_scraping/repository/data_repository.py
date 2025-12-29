"""Data repository definition."""
from typing import Dict
import copy

class DataRepository:
    """Storage in memory of the scraped data."""
    stock_data: Dict = {}
    profile_data: Dict = {}
    stats_data: Dict = {}
    holders_data: Dict = {}

    def insert_stock_data(self, stock_data: Dict) -> None:
        """Method to add rows the stocks data."""
        self.stock_data.update(stock_data)

    def insert_profile_data(self, profile_data: Dict) -> None:
        """Method to add rows the profile data."""
        self.profile_data.update(profile_data)

    def insert_stats_data(self, stats_data: Dict) -> None:
        """Method to add rows the stats data."""
        self.stats_data.update(stats_data)

    def insert_holders_data(self, holder_data: Dict) -> None:
        """Method to add rows the holder data."""
        self.holders_data.update(holder_data)

    def get_youngest_ceos(self, limit: int) -> Dict:
        """Get stocks with the youngest CEOs."""
        joined_dict = copy.deepcopy(dict(sorted(
            self.profile_data.items(),
            key=lambda profile:(
                profile[1]['ceo_year_born'] is not None,
                profile[1]['ceo_year_born']),
            reverse=True)[:limit]))

        # Join the name
        for key, _ in joined_dict.items():
            joined_dict[key]['name'] = self.stock_data[key]
        return joined_dict

    def get_best_change(self, limit: int) -> Dict:
        """Get stocks with the best 52 week change."""
        joined_dict = copy.deepcopy(dict(sorted(
            self.stats_data.items(),
            key=lambda stat:(
                stat[1]['week_change_52'] is not None,
                stat[1]['week_change_52']),
            reverse=True)[:limit]))

        # Join the name
        for key, _ in joined_dict.items():
            joined_dict[key]['name'] = self.stock_data[key]
        return joined_dict

    def get_largest_holds(self, limit: int) -> Dict:
        """Get stocks with the largest holds of Blackrock Inc."""
        joined_dict = copy.deepcopy(dict(sorted(
            self.holders_data.items(),
            key=lambda hold:(
                hold[1]['shares'] is not None,
                hold[1]['shares']),
            reverse=True)[:limit]))

        # Join the name
        for key, _ in joined_dict.items():
            joined_dict[key]['name'] = self.stock_data[key]
        return joined_dict
