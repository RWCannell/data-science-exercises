from get_wikipedia_table import *

country_population_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
country_obesity_rate_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_obesity_rate'
country_hdi_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index'
country_alcohol_consumption_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_alcohol_consumption_per_capita'
    
if __name__ == '__main__':
    df = get_wikipedia_table(country_population_wiki_url, 0)[0]
    country_population_df = df.iloc[:, [1,2]]
    print(country_population_df)
    # country_population_df.to_csv('country_population_wikipedia_data.csv')

