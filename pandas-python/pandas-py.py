import pandas as pd

bios = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv')

height_input = float(input(" ennter the minimum of hight"))
tall_people = bios.loc[bios["height_cm"] > height_input, ["name", "height_cm"]]
print(tall_people)