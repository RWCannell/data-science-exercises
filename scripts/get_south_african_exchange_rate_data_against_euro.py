import pandas as pd

full_exchange_rates_df = pd.read_csv("csv/exchange_rates_against_euro.csv")

selected_currency = 'ZAR'
south_african_exchange_rates_df = full_exchange_rates_df[full_exchange_rates_df['currency'].str.contains(selected_currency)]

csv_name = "south_african_exchange_rate_against_euro.csv"
south_african_exchange_rates_df.to_csv(f"csv\{csv_name}")