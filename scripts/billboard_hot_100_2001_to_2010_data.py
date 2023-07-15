import pandas as pd

df_2001 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2001_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2002 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2002_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2003 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2003_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2004 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2004_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2005 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2005_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2006 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2006_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2007 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2007_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2008 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2008_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2009 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2009_data.csv', usecols = ['date','rank', 'artist', 'song'])
df_2010 = pd.read_csv('csv/billboard_hot_100/billboard_hot_100_2010_data.csv', usecols = ['date','rank', 'artist', 'song'])

df_2001_to_2010 = pd.concat([
    df_2001, 
    df_2002,
    df_2003,
    df_2004,
    df_2005,
    df_2006,
    df_2007,
    df_2008,
    df_2009,
    df_2010,
])

top_three_df_2001_to_2010 = df_2001_to_2010[df_2001_to_2010['rank'] < 4]

artist_with_most_top_three_appearances = top_three_df_2001_to_2010['artist'].value_counts().idxmax()
number_of_occurrences = top_three_df_2001_to_2010['artist'].value_counts()[0]

print(f"Artist with most top 3 appearances between 2001 to 2010: {artist_with_most_top_three_appearances} with {number_of_occurrences} appearances") 