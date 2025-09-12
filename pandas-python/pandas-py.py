import pandas as pd

bios = pd.read_csv('https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv')

print(bios.head(3))
print(bios.info())
height_input = float(input(" enter the minimum hight "))
tall_people = bios.loc[bios["height_cm"] > height_input, ["name", "height_cm"]]
print(tall_people)