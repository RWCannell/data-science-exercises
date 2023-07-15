import pandas as pd

df_2011 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2011_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2012 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2012_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2013 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2013_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2014 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2014_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2015 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2015_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2016 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2016_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2017 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2017_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2018 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2018_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2019 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2019_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2020 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2020_data.csv', usecols = ['date','rank', 'artist', 'song'])

df_2011_to_2020 = pd.concat([
    df_2011, 
    df_2012,
    df_2013,
    df_2014,
    df_2015,
    df_2016,
    df_2017,
    df_2018,
    df_2019,
    df_2020,
])

top_three_df_2011_to_2020 = df_2011_to_2020[df_2011_to_2020['rank'] < 4]

artist_with_most_top_three_appearances = top_three_df_2011_to_2020['artist'].value_counts().idxmax()
number_of_occurrences = top_three_df_2011_to_2020['artist'].value_counts()[0]

print(f"Artist with most top 3 appearances between 2011 to 2020: {artist_with_most_top_three_appearances} with {number_of_occurrences} appearances") 