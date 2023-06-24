import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_wikipedia_table(wiki_url, table_index):
    response = requests.get(wiki_url)
    successfulResponse = False
    response_code = response.status_code

    if response_code == 200:
        successfulResponse = True
        print(f"Successful request to Wikipedia: {wiki_url}")
    else:
        print(f"Failed request to Wikipedia: {wiki_url}")

    if successfulResponse:
        soup = BeautifulSoup(response.text, 'html.parser')
        countries_population = soup.find_all('table', {"class": "wikitable", "class": "sortable"})
        if len(countries_population) == 0:
            print('No tables are present')
        tables = pd.read_html(str(countries_population[table_index]))
        print(tables)
        return tables