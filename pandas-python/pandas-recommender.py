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

def helper_budget() :
    pass


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

'''
statistics related to duration:
shortest film
longest film
mean duration
'''
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

'''
statistics related to rating:
mean rating
median rating
'''
def stat_rating() -> None:
    mean_rating : float = round(movies['rating'].mean(), 2)
    print("mean rating ", mean_rating)
    median_rating : float = movies['rating'].median()
    print("median rating ", median_rating)


def stat_name() -> None:
    print(movies['name'].values)
    print(movies['name'].iloc[0])
    print(type(movies['name'].iloc[0]))
    print(len(movies['name'].iloc[0]))
    # df['name'].iloc[0]

def stat_budget() -> None:
    # print(movies['budget'].values)
    # print(type(movies.loc[0, 'budget']))
    # print("here   ")

    # the most expensive film
    biggest_budget : int = movies_new_df['budget'].max()
    expensive_film = movies_new_df.loc[movies_new_df['budget'] == biggest_budget]
    print("the most expensive film is ", expensive_film[['name', 'rank', 'budget']])

    # the cheapest film
    smallest_budget : int = movies_new_df[movies_new_df['budget'] != -1]['budget'].min()
    cheapest_film = movies_new_df.loc[movies_new_df['budget'] == smallest_budget]
    print("the most cheapest film is ", cheapest_film[['name', 'rank', 'budget']])



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

print(movies_new_df.info())
# stat_run_time()
# stat_rating()
# stat_budget()

# to change budget
movies_new_df['budget'] = movies_new_df['budget'].astype(str)
movies_new_df['budget'] = movies_new_df['budget'].replace('Not Available', '-1')
# print(movies_new_df.loc[movies_new_df['budget'] == '-1', ['name', 'budget']])
# print(movies_new_df.loc[movies_new_df['budget'] == '-1', ['name', 'budget', 'box_office']])
# stat_budget()

# to change box_office
movies_new_df['box_office'] = movies_new_df['box_office'].astype(str)
movies_new_df['box_office'] = movies_new_df['box_office'].replace('Not Available', '-1')
stat_budget()


