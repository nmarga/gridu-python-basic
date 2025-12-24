"""Parser definition"""
from typing import List
from bs4 import BeautifulSoup

class Parser:
    """Parser has the role to parse the raw scraped data into readable format."""

    @staticmethod
    def parse_stocks(html_content: str) -> List:
        """Method to parse stocks html data"""
        soup = BeautifulSoup(html_content, 'html.parser')
        data_list = []
        stock_list = []

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

            stock_list.append(stock_data)
        print(stock_list)
        return stock_list

    @staticmethod
    def parse_profile(html_content: str) -> List:
        """Method to parse profile of a stock html data."""
        return [html_content]
