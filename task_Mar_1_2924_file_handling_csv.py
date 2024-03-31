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

import pandas as pd

# Read the existing CSV file into a DataFrame
existing_df = pd.read_csv("data.csv")

# Create a new DataFrame with the data you want to append
new_data = {'username': ['user1', 'user2'], 'password': ['pass456', 'pass789']}
new_df = pd.DataFrame(new_data)

# Concatenate the existing DataFrame and the new DataFrame
concatenated_df = pd.concat([existing_df, new_df], ignore_index=True)

# Write the concatenated DataFrame back to the CSV file
concatenated_df.to_csv("data.csv", index=False)


