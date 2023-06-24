from get_wikipedia_table import *

country_homicide_rate_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate'
    
if __name__ == '__main__':
    df = get_wikipedia_table(country_homicide_rate_wiki_url, 1)[0]
    country_homicide_rate_df = df.iloc[:, [0,3]]
    print(country_homicide_rate_df)
    # country_homicide_rate_df.to_csv('country_homicide_rate_wikipedia_data.csv')

