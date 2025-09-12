import os
import numpy as np
import pandas as pd

'''

'''
def convert_time_int(str_time : str) -> int:
    hours : int = 0
    min : int = 0

    if 'h' in str_time:
        hours_part = str_time.split('h')[0]
        hours = int(hours_part.strip())
        str_time = str_time.split('h')[1] 
    
    if 'm' in str_time:
        minutes_part = str_time.split('m')[0]
        minutes = int(minutes_part.strip())
    
    return hours * 60 + minutes

def stat_box_office() -> None:
    print(df['box_office'].values)

'''
statistics related to time:
the oldest film
the newest film
number of films per year
'''
def stat_year() -> None:
    newest_year : int = df['year'].min()
    newest_film = df.loc[df['year'] == newest_year]
    print("the newest film is \n", newest_film)

    oldest_year : int = df['year'].max()
    oldest_film = df.loc[df['year'] == oldest_year]
    print("the oldest film is \n", oldest_film)
    
    year_counts = df['year'].value_counts()
    year_counts_sorted = year_counts.sort_values(ascending=False)
    print("number of films per year \n")
    print(year_counts_sorted.head(5))

def stat_certificate() -> None:
    pass

def stat_run_time() -> None:
    print(df['run_time'].values)
    example = df.loc[0, 'run_time']
    print(example)
    # print("here  ", type(example))
    print(convert_time_int(example))

def new_data() -> None:
    new_data = df.copy()
    new_data.to_parquet("IMDBTop250Movies_new.parquet", engine='pyarrow', index=False)
    print(new_data.info())


def stat_tagline() -> None:
    # print(df['tagline'].values)
    pass

def stat_rating() -> None:
    mean_rating : float = df['rating'].mean()
    print("mean_rating ", mean_rating)
    median_rating : int = df['rating'].median()
    print("median_rating ", median_rating)

def stat_name() -> None:
    print(df['name'].values)
    print(df['name'].iloc[0])
    print(type(df['name'].iloc[0]))
    print(len(df['name'].iloc[0]))
    # df['name'].iloc[0]

def stat_budget() -> None:
    print(df['budget'].values)


def to_prepare_statistic() -> None:
    df['directors'] = df['directors'].str.split(',')

def to_parquet(filename : str) -> None :
    if filename.lower().endswith('.csv'):
        df.to_parquet("bios_new.parquet", engine='pyarrow', index=False)

def movie_statistics()-> None:
    unique_genre : int = df['genre'].nunique()
    list_genres = df['genre'].unique()
    print(list_genres)





filename = 'IMDBTop250Movies.csv'
df = pd.read_csv(filename)
print(df.info())
stat_run_time()
# stat_name()


