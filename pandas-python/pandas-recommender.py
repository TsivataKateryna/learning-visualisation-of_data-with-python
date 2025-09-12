import os
import numpy as np
import pandas as pd

def convert_time_int(str_time : str) -> int:
    hours : int = 0
    min : int = 0

    if 'h' in duration:
        hours_part = duration.split('h')[0]
        hours = int(hours_part.strip())
        duration = duration.split('h')[1] 
    
    if 'm' in duration:
        minutes_part = duration.split('m')[0]
        minutes = int(minutes_part.strip())
    
    return hours * 60 + minutes

def stat_box_office() -> None:
    print(df['box_office'].values)

''
def stat_year() -> None:
    the_earliest_year : int = df['year'].min()
    the_earliest_film = df.loc[df['year'] == the_earliest_year]
    # print(" sidoiervner", type(the_earliest_film))
    print("the_earliest_film \n", the_earliest_film)

    the_oldest_year : int = df['year'].max()
    the_oldest_film = df.loc[df['year'] == the_oldest_year]
    print("the_oldest_film \n", the_oldest_film)
    
    print("Number of films per year")
    year_counts = df['year'].value_counts()
    year_counts_sorted = year_counts.sort_values(ascending=False)
    print(year_counts_sorted.head(5))

def stat_certificate() -> None:
    pass

def stat_run_time() -> None:
    print(df['run_time'].values)

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
stat_name()

# stat_rating()
# stat_tagline()
# stat_run_time()
# stat_budget()
# new_data()

# print(df.head())
# print(df['rating'])
# stat_rating()
# stat_year()
# print(df['certificate'])
# print(df['box_office'].values)
# print(df['directors'].values)
# to_prepare_statistic()
# print(df['directors'].values)
# print(df['directors'].nunique())
# print(df['genre'].unique())
# print(df['genre'].nunique())

# print(df[['name','year','genre']].head())
# print(df.columns)
# print(type(df)) # <class 'pandas.core.frame.DataFrame'>
# movie_statistics()

# stat_box_office()
