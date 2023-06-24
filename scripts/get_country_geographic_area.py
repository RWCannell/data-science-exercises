from get_wikipedia_table import *

country_geographic_area_wiki_url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area'
    
if __name__ == '__main__':
    df = get_wikipedia_table(country_geographic_area_wiki_url, 0)[0]
    country_geographic_area_df = df.iloc[:, [1,2,3,4,5]]
    print(country_geographic_area_df)
    # country_geographic_area_df.to_csv('country_geographic_area_wikipedia_data.csv')

