"""Parser definition"""
from bs4 import BeautifulSoup
from typing import List

class Parser:
    """Parser has the role to parse the raw scraped data into readable format"""

    @staticmethod
    def parse(html_content: str) -> List:
        soup = BeautifulSoup(html_content, 'html.parser')

        data_list = []
        table_content = soup.find('tbody')
        if table_content:
            data_list = table_content.find_all('tr')
        for data in data_list:
            for row in data.find_all('td'):
                div_content = row.find('div')
                if div_content:
                    print(div_content.text)
        return data_list
