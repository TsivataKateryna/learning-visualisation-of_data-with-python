import os
import numpy as np
import pandas as pd

'''

'''
def convert_time_int(str_time : str) -> int:
    if(str_time == "Not Available"): return -1
    hours : int = 0
    minutes : int = 0

    if 'h' in str_time:
        hours_part = str_time.split('h')[0]
        hours = int(hours_part.strip())
        str_time = str_time.split('h')[1] 
    
    if 'm' in str_time:
        minutes_part = str_time.split('m')[0]
        minutes = int(minutes_part.strip())
    
    return hours * 60 + minutes

def stat_box_office() -> None:
    print(movies['box_office'].values)

'''
statistics related to time:
the oldest film
the newest film
number of films per year
'''
def stat_year() -> None:
    newest_year : int = movies['year'].min()
    newest_film = movies.loc[movies['year'] == newest_year]
    print("the newest film is \n", newest_film)

    oldest_year : int = movies['year'].max()
    oldest_film = movies.loc[movies['year'] == oldest_year]
    print("the oldest film is \n", oldest_film)
    
    year_counts = movies['year'].value_counts()
    year_counts_sorted = year_counts.sort_values(ascending=False)
    print("number of films per year \n")
    print(year_counts_sorted.head(5))

def stat_certificate() -> None:
    pass

def stat_run_time() -> None:
    # shortest film
    shortest_duration : int = movies_new_df[movies_new_df['run_time_min'] != -1]['run_time_min'].min()
    shortest_film = movies_new_df.loc[movies_new_df['run_time_min'] == shortest_duration]
    print("the shortest film is (where time is available)\n", shortest_film[['name', 'directors', 'run_time', 'run_time_min']])
    
    # longest film
    longest_duration : int = movies_new_df[movies_new_df['run_time_min'] != -1]['run_time_min'].max()
    longest_film = movies_new_df.loc[movies_new_df['run_time_min'] == longest_duration]
    print("the longest film is (where time is available)\n", longest_film[['name', 'directors', 'run_time', 'run_time_min']])

    # mean duration
    mean_dur : float = movies_new_df[movies_new_df['run_time_min'] != -1]['run_time_min'].mean()
    mean_duration : float = round(mean_dur, 2)
    print("on average, films last :", mean_duration, " minutes, or ")
    hours = int(mean_duration // 60)
    minutes = int(round(mean_duration - hours * 60))
    print(hours, "h ", minutes , "m")


def stat_tagline() -> None:
    # print(movies['tagline'].values)
    pass

def stat_rating() -> None:
    mean_rating : float = movies['rating'].mean()
    print("mean_rating ", mean_rating)
    median_rating : int = movies['rating'].median()
    print("median_rating ", median_rating)

def stat_name() -> None:
    print(movies['name'].values)
    print(movies['name'].iloc[0])
    print(type(movies['name'].iloc[0]))
    print(len(movies['name'].iloc[0]))
    # df['name'].iloc[0]

def stat_budget() -> None:
    print(movies['budget'].values)

def to_prepare_statistic() -> None:
    movies['directors'] = movies['directors'].str.split(',')

def to_parquet(filename : str) -> None :
    if filename.lower().endswith('.csv'):
        movies.to_parquet("bios_new.parquet", engine='pyarrow', index=False)

def movie_statistics()-> None:
    unique_genre : int = movies['genre'].nunique()
    list_genres = movies['genre'].unique()
    print(list_genres)


filename = 'IMDBTop250Movies.csv'
movies = pd.read_csv(filename)
movies_new_df = movies.copy()
movies_new_df.to_parquet("IMDBTop250Movies_new.parquet", engine='pyarrow', index=False)
movies_new_df['run_time_min'] = movies['run_time'].apply(convert_time_int)
# print(movies_new_df[movies_new_df['run_time'] == "Not Available"][['name', 'directors', 'run_time', 'run_time_min']])

stat_run_time()



