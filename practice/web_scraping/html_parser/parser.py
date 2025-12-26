"""Parser definition"""
from typing import Dict
import re
from bs4 import BeautifulSoup

class Parser:
    """Parser has the role to parse the raw scraped data into readable format."""

    @staticmethod
    def parse_stocks(html_content: str) -> Dict:
        """Method to parse stocks html data"""
        soup = BeautifulSoup(html_content, 'html.parser')
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
        # print(stock_dict)
        return stock_dict

    @staticmethod
    def parse_profile(html_content: str, tag: str) -> Dict:
        """Method to parse profile of a stock html data."""
        soup = BeautifulSoup(html_content, 'html.parser')
        profile_data = {}
        profile_data[tag] = {}

        # Extract the address of the company
        address_content = soup.find('div', class_=re.compile(r'address yf-.*'))
        if address_content:
            profile_data[tag]['country'] = address_content.find_all('div')[-1].text
        print(address_content)

        # Extract the stats of the company and find the number of employees
        company_stats_content = soup.find('dl', class_=re.compile(r'company-stats yf-.*'))
        if company_stats_content:
            employee_stats = company_stats_content.find_all('dd')[-1]

            if employee_stats:
                profile_data[tag]['employees'] = int(employee_stats.text.replace(',', ''))
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
            profile_data[tag]['year_born'] = company_ceo_data.find_all('td')[-1].text.strip()

        print(profile_data)
        return profile_data
