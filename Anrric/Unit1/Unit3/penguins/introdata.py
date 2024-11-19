#import data tools 
import pandas as pd 
import plotly.express as px 


# read in the data from our csv (located in the same folder)
dataframe = pd.read_csv("penguins.csv")


#---------------------------------------------------useful dataframe functions ----------------------


#print out a summary of our data 
summary = dataframe.describe()
print("summary:", summary)

#Print out the data types of each column 

types = dataframe.info()
print("types:", types)

#print out the first 5 rows of our data frame 

head = dataframe.head()
print("head:", head)


print("dimensions", dataframe.shape)

#--------------------------------Plot Data----------------------------------------------

#px.scatter(dataframe, x = "flipper_length", y = "beak_length_mm", color = "species", symbol = "island").show()


#----------------------------How to index into your dataframe---------------------------------

#read the island of the 5th penguin 
print(dataframe["island"][4])

# we want to read the beakheightmm of our 10th penguin 

print((dataframe)["beak_height_mm"][9])

#we want to read the entire row of our 12th penguin

for i in range(7):
    print((dataframe.columns[i]), ":", dataframe[dataframe.columns[i]][11])