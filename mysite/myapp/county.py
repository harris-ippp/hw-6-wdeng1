import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

elections = []

for line in open("ELECTION_ID"):
    a = line.split()
    year = a[0]+".csv"

    header = pd.read_csv(year, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

    df = pd.read_csv(year, index_col = 0, thousands = ",", skiprows = [1])

    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = a[0]
    elections.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])

all = pd.concat(elections)
df.to_csv("county.csv")
