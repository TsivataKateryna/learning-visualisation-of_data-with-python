import pandas as pd
import numpy as np
import os

# possible_choice = ['', '', '']

def to_parquet(df) -> None :
    df.to_parquet("bios_new.parquet", engine='pyarrow', index=False)


def chose():
    pass




df = pd.read_csv('./my_data_kaggle/IMDBTop250Movies.csv')
# print(df.type)
print(os.path.exists('data/IMDBTop250Movies.csv'))
print(os.getcwd())  
print(os.listdir()) 