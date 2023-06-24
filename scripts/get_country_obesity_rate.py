from get_wikipedia_table import *

country_obesity_rate_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_obesity_rate'
    
if __name__ == '__main__':
    df = get_wikipedia_table(country_obesity_rate_wiki_url, 0)[0]
    country_obesity_rate_df = df.iloc[:, [0,1]]
    print(country_obesity_rate_df)
    # country_obesity_rate_df.to_csv('country_obesity_rate_wikipedia_data.csv')

