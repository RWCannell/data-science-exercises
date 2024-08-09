import pandas as pd

full_exchange_rates_df = pd.read_csv("csv/exchange_rates_against_euro.csv")

selected_currency = 'ZAR'
full_south_african_exchange_rates_df = full_exchange_rates_df[full_exchange_rates_df['currency'].str.contains(selected_currency)]

desired_columns = [
    'date',
    'currency',
    'value'
]


south_african_exchange_rates_df = full_south_african_exchange_rates_df[desired_columns]

south_african_exchange_rates_df.reset_index(drop=True, inplace=True)

south_african_exchange_rates_df['date'] = pd.to_datetime(south_african_exchange_rates_df['date'], dayfirst=True)
south_african_exchange_rates_df['value']= pd.to_numeric(south_african_exchange_rates_df['value'])

csv_name = "south_african_exchange_rate_against_euro.csv"
south_african_exchange_rates_df.to_csv(f"csv\{csv_name}")
