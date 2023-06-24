import pandas as pd
import requests
from bs4 import BeautifulSoup

country_population_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
country_homicide_rate_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate'
country_area_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area'
country_obesity_rate_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_obesity_rate'
country_hdi_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index'
country_alcohol_consumption_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_alcohol_consumption_per_capita'

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
        return tables
    

if __name__ == '__main__':
    df = get_wikipedia_table(country_population_wiki_url, 0)[0]
    country_population_df = df.iloc[:, [1,2]]
    print(country_population_df)
    country_population_df.to_csv('country_population_wikipedia_data.csv')

