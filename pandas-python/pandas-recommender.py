import os
import numpy as np
import pandas as pd

# possible_choice = ['', '', '']
def stat_box_office() -> None:
    pass

def stat_year() -> None:
    the_earliest_year : int = df['year'].min()
    the_earliest_film = df.loc[df['year'] == the_earliest_year, ['name', 'year']]
    print("the_earliest_film ", the_earliest_film)
    pass

def stat_rating() -> None:
    mean_rating : float = df['rating'].mean()
    print("here ", mean_rating)
    pass

def to_prepare_statistic() -> None:
    df['directors'] = df['directors'].str.split(',')

def to_parquet(filename : str) -> None :
    if filename.lower().endswith('.csv'):
        df.to_parquet("bios_new.parquet", engine='pyarrow', index=False)

def movie_statistics()-> None:
    unique_genre : int = df['genre'].nunique()
    list_genres = df['genre'].unique()
    # print(list_genres)



    pass

def chose(filename):
    df = pd.read_csv(filename)
    to_parquet(filename)


    pass


filename = 'IMDBTop250Movies.csv'
df = pd.read_csv(filename)
print(df.info())

# print(df.head())
# print(df['rating'])
# stat_rating()
stat_year()
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
