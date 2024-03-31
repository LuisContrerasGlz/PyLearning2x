# Using CSV

import csv

import pandas as pd

with open("data.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[0], row[1], sep="-")


# Using pandas
        
df = pd.read_csv("data.csv")
print(df)

