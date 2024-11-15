# Import data tools
import pandas as pd
import plotly.express as px

# Read in the data from our csv (located in the same folder)
dataframe = pd.read_csv("penguins.csv")

# ------------------------ Useful dataframe functions ------------------------

# Print out a summary of our data
summary = dataframe.describe()
print("summary:", summary)

# Print out the data types of each column
types = dataframe.info()
print("types:", types)

# Print out the first 5 rows of our dataframe
head = dataframe.head()
print("head:", head)

# Print out the dimensions of our dataframe
print("dimensions:", dataframe.shape)

# ---------------------------- Plot data ----------------------------

# px.scatter(dataframe, x = "flipper_length", y = "beak_length_mm", color = "species", symbol = "island").show()

# ---------------------------- Plot data ----------------------------

# Read the island of the 5th penguin
print(dataframe["island"][4])

# Read the beak_height_mm of our 10th penguin
print(dataframe["beak_height_mm"][9])

# Read the entire row of our 12th penguin
for i in range(7):
    print(dataframe.columns[i], ": ", dataframe[dataframe.columns[i]][11])



'''
print(dataframe.head())
print(dataframe.columns.to_list())
print(dataframe.dtypes)
'''
