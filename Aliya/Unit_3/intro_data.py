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

'''
print(dataframe.head())
print(dataframe.columns.to_list())
print(dataframe.dtypes)
'''
