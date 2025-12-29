"""Parser definition."""
from typing import Dict
import re
from bs4 import BeautifulSoup

class Parser:
    """Parser has the role to parse the raw scraped data into readable format."""
    @staticmethod
    def parse_stocks(html_content: str) -> Dict:
        """Method to parse stocks html data."""
        soup = BeautifulSoup(html_content, 'lxml')
        data_list = []
        stock_dict = {}

        # Find the main table body
        table_content = soup.find('tbody')

        # Extract the raw data rows
        if table_content:
            data_list = table_content.find_all('tr')

        for data in data_list:
            # Set stock data as a dictionary with tag as key and name as value
            stock_data = {}
            tag = ""
            for cell in data.find_all('td'):
                div_content = cell.find('div')
                if not div_content:
                    break
                # Set the first cell in the row as key and second as the value
                if not stock_data:
                    tag = div_content.text.strip()
                    stock_data[tag] = None
                elif not stock_data[tag]:
                    stock_data[tag] = div_content.text.strip()
            stock_dict.update(stock_data)

        return stock_dict

    @staticmethod
    def parse_profile(html_content: str, tag: str) -> Dict:
        """Method to parse profile of a stock html data."""
        soup = BeautifulSoup(html_content, 'lxml')
        profile_data = {}
        profile_data[tag] = {}
        profile_data[tag]['country'] = None
        profile_data[tag]['employees'] = None
        profile_data[tag]['ceo_name'] = None
        profile_data[tag]['ceo_year_born'] = None

        # Extract the address of the company
        address_content = soup.find('div', class_=re.compile(r'address yf-.*'))
        if address_content:
            profile_data[tag]['country'] = address_content.find_all('div')[-1].text

        # Extract the stats of the company and find the number of employees
        company_stats_content = soup.find('dl', class_=re.compile(r'company-stats yf-.*'))
        if company_stats_content:
            employee_stats = company_stats_content.find_all('dd')[-1]

            if employee_stats:
                try:
                    profile_data[tag]['employees'] = int(
                        employee_stats.text.strip().replace(',',''))
                except ValueError:
                    profile_data[tag]['employees'] = None
        company_table_content = soup.find('table', class_=re.compile(r'yf-.*'))

        # Extract the company's CEO data find his name and age
        company_ceo_data = None
        if company_table_content:
            table_content_rows = company_table_content.find_all('tr')

            for table_content_row in table_content_rows:
                if 'CEO' in table_content_row.text:
                    company_ceo_data = table_content_row
                    break

        if company_ceo_data:
            profile_data[tag]['ceo_name'] = company_ceo_data.find_all('td')[0].text.strip()
            try:
                profile_data[tag]['ceo_year_born'] = int(
                    company_ceo_data.find_all('td')[-1].text.strip())
            except ValueError:
                profile_data[tag]['ceo_year_born'] = None

        return profile_data

    @staticmethod
    def parse_stats(html_content: str, tag: str) -> Dict:
        """Method to parse stats of a stock html data."""
        soup = BeautifulSoup(html_content, 'lxml')
        stats_data = {}
        stats_data[tag] = {}
        stats_data[tag]['week_change_52'] = None
        stats_data[tag]['total_cash'] = None

        # Extract the 52 week change of the company
        stats_table = soup.find_all('table')
        change_stats_table = None
        stats_list_table = None
        for table in stats_table:
            if '52 Week Change' in table.get_text():
                change_stats_table = table
            if 'Market Cap' in table.get_text():
                stats_list_table = table

        # Extract the 52 week change
        if change_stats_table:
            week_change = change_stats_table.find_all('tr')[1].find_all('td')[1]
            if week_change:
                try:
                    stats_data[tag]['week_change_52'] = float(
                        week_change.text.strip().replace('%', ''))
                except ValueError:
                    stats_data[tag]['week_change_52'] = None

        # Extract the total company market cap
        if stats_list_table:
            market_cap = stats_list_table.find_all('tr')[1].find_all('td')[1]
            if market_cap:
                stats_data[tag]['total_cash'] = market_cap.text.strip()

        return stats_data

    @staticmethod
    def convert_to_int(num_str: str) -> int:
        """Helper method to convert to integer nubmers with M and B postfix."""
        powers = {'M': 10**6, 'B': 10**9}
        # Regex to find number part and optional suffix
        match = re.search(r"([0-9\.]+)\s?([MB])", num_str, re.IGNORECASE)
        if match:
            quantity = float(match.group(1))
            magnitude = match.group(2).upper()
            return int(quantity * powers[magnitude])
        else:
            return int(num_str)

    @staticmethod
    def parse_holders(html_content: str, tag: str) -> Dict:
        """Method to parse stats of a stock html data."""
        soup = BeautifulSoup(html_content, 'lxml')
        holders_data = {}
        holders_data[tag] = {}
        holders_data[tag]['shares'] = None
        holders_data[tag]['date_reported'] = None
        holders_data[tag]['per_out'] = None
        holders_data[tag]['value'] = None

        # Get the Top Institutional Holders table
        holders_table = soup.find_all('table')[1]

        holders = holders_table.find_all('tr') if holders_table else []

        # Extract the the row where Blackrock holds the shares
        for holder in holders:
            if 'Blackrock' in holder.get_text():
                try:
                    holders_data[tag]['shares'] = Parser.convert_to_int(
                        holder.find_all('td')[1].text.strip())
                except ValueError:
                    holders_data[tag]['shares'] = None
                holders_data[tag]['date_reported'] = holder.find_all('td')[2].text.strip()
                holders_data[tag]['per_out'] = holder.find_all('td')[3].text.strip()
                holders_data[tag]['value'] = holder.find_all('td')[4].text.strip()
                break

        return holders_data
