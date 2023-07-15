import pandas as pd

df_1991 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_1991_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_1992 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_1992_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_1993 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_1993_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_1994 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_1994_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_1995 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_1995_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_1996 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_1996_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_1997 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_1997_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_1998 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_1998_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_1999 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_1999_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2000 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2000_data.csv', usecols = ['date','rank', 'artist', 'song'])

df_1991_to_2000 = pd.concat([
    df_1991, 
    df_1992,
    df_1993,
    df_1994,
    df_1995,
    df_1996,
    df_1997,
    df_1998,
    df_1999,
    df_2000,
])

top_three_df_1991_to_2000 = df_1991_to_2000[df_1991_to_2000['rank'] < 4]

artist_with_most_top_three_appearances = top_three_df_1991_to_2000['artist'].value_counts().idxmax()
number_of_occurrences = top_three_df_1991_to_2000['artist'].value_counts()[0]

print(f"Artist with most top 3 appearances between 1991 to 2000: {artist_with_most_top_three_appearances} with {number_of_occurrences} appearances") 