import pandas as pd

df = pd.read_csv("data/cfa-data.csv", sep="\t")


print(df['NameOfTheTopic'])