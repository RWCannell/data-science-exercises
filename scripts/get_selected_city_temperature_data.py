import pandas as pd

# this dataset is NOT included in the repository due to its size
full_city_temperature_df = pd.read_csv("csv/city_temperature.csv")

country = 'Morocco'
country_cities_temperature_df = full_city_temperature_df[full_city_temperature_df['Country'].str.contains(country)]

country_name = country.lower()

contains_spaces = False
if ' ' in country:
    country_name = country_name.replace(' ', '_')

csv_name = f"{country_name}_cities_temperature_data.csv"
country_cities_temperature_df.to_csv(f"csv\city_temperature_data\{csv_name}")