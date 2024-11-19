# import data tools
import pandas as pd
import plotly.express as px

# read in the data from our csv (located in the same folder)
dataframe = pd.read_csv("penguins.csv")

# --------------------------------- Useful dataframe functions ------------------------------------------

# Print out a summary of our data
summary = dataframe.describe()
print("summary: ", summary)

# print out the data types of each column

types = dataframe.info()
print("types", types)

# print out the first 5 rows of our dataframe

head = dataframe.head()
print("head: ", head)

print("dismensions", dataframe.shape)

# ----------------------------------------- Plot data --------------------------------------------------

px.scatter(dataframe, x="gender", y="body_mass_g", color="species", symbol="island").show()

# ----------------------------- How to index into our dataframe ----------------------------------------

# read the island of the 5th penguin
print(dataframe["island"][4])


# want to read the beak_height_mm of our 10th penguin

print(dataframe["beak_height_mm"][9])

# we want to read the entire row of our 12th penguin
for i in range(7):
    print(dataframe.columns[i], ": ", dataframe[dataframe.columns[i]][11])
