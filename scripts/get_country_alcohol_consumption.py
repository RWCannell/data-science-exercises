from get_wikipedia_table import *

country_alcohol_consumption_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_alcohol_consumption'
    
if __name__ == '__main__':
    df = get_wikipedia_table(country_alcohol_consumption_wiki_url, 0)[0]
    country_alcohol_consumption_df = df.iloc[:]
    print(country_alcohol_consumption_df)
    # country_alcohol_consumption_df.to_csv('country_alcohol_consumption_wikipedia_data.csv')

