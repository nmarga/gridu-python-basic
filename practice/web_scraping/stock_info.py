"""
There is a list of most active Stocks on Yahoo Finance https://finance.yahoo.com/most-active.
You need to compose several sheets based on data about companies from this list.
To fetch data from webpage you can use requests lib. To parse html you can use beautiful soup lib or lxml.
Sheets which are needed:
1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.


Example for the first sheet (you need to use same sheet format):
==================================== 5 stocks with most youngest CEOs ===================================
| Name        | Code | Country       | Employees | CEO Name                             | CEO Year Born |
---------------------------------------------------------------------------------------------------------
| Pfizer Inc. | PFE  | United States | 78500     | Dr. Albert Bourla D.V.M., DVM, Ph.D. | 1962          |
...

About sheet format:
- sheet title should be aligned to center
- all columns should be aligned to the left
- empty line after sheet

Write at least 2 tests on your choose.
Links:
    - requests docs: https://docs.python-requests.org/en/latest/
    - beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - lxml docs: https://lxml.de/
"""
import os
from typing import List, Union, Dict
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

def scrape_website(url: str, headers_content: Dict) -> Union[List, None]:
    try:
        response = requests.get(url, timeout=3, headers=headers_content)
        print(response.headers)
        print(response)
        html_content = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

    soup = BeautifulSoup(html_content, 'html.parser')

    data_list = []
    data_list.append(soup.find('table'))

    return data_list


if __name__ == "__main__":
    # Load from .env file
    load_dotenv()

    USER_AGENT = os.getenv("USER_AGENT", "")
    TARGET_URL = os.getenv("TARGET_URL", "")

    headers = {
        'User-Agent': USER_AGENT
    }

    scraped_data = scrape_website(TARGET_URL, headers)

    if scraped_data:
        print(f"Scraped {len(scraped_data)} data points from {TARGET_URL}\n")
        # Print the first few results
        for item in scraped_data[:10]:
            print(f"Text: {scraped_data}")
    else:
        print("Scraping failed or no data found.")
