from get_wikipedia_table import *

country_hdi_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index'
    
if __name__ == '__main__':
    df = get_wikipedia_table(country_hdi_wiki_url, 0)[0]
    country_hdi_df = df.iloc[:, [2,3]]
    print(country_hdi_df)
    # country_hdi_df.to_csv('country_hdi_wikipedia_data.csv')

