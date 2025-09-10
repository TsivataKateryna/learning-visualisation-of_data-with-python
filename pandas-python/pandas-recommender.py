import pandas as pd
import numpy as np
import os

# possible_choice = ['', '', '']

def to_parquet(filename : str) -> None :
    if filename.lower().endswith('.csv'):
        df.to_parquet("bios_new.parquet", engine='pyarrow', index=False)

def chose(filename):
    df = pd.read_csv(filename)
    to_parquet(filename)


    pass


filename = 'IMDBTop250Movies.csv'
df = pd.read_csv(filename)
# print(df.info)
# print(df[['name','year','genre']].head())
# print(df.info())
# print(df.columns)
print(type(df)) # <class 'pandas.core.frame.DataFrame'>

