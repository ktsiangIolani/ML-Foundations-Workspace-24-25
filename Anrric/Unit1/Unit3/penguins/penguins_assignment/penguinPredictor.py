# Name:
# ML Foundations 24-25
# Supervised Learning - Penguins.csv

# THE GOAL
# This program will take in data about a penguin and predict what species it is

# THE DATA
# There are two data sets in this folder:
# Use the penguins in penguins_train.csv as the data for this program
# Use the penguins in penguins_test.csv to test your program and see how accurate it is

#import necessary python tools
import pandas as pd

#This function take in data about the penguin. It must be entered as island, beak length, beak height, flipper length, body_mass, gender
def get_penguin_info():
    penguinInfo = []
    while(len(penguinInfo) != 6):
        penguinInfo = input("Enter in data about the penguin you want to identify: ").split(",")

    print("We will now predict the species of the following penguin:" + "\n" + "Island: " + penguinInfo[0] + "\n" + "Beak Length: " + penguinInfo[1] + "\n" + "Beak Height: " + penguinInfo[2] + "\n" + "Flipper Length: " + penguinInfo[3] + "\n" + "Body Mass: " + penguinInfo[4], "Gender: " + penguinInfo[5])
    return penguinInfo

#read the data from its csv file
dataframe = pd.read_csv("penguins_train.csv")

# TODO 1: complete the function predict_penguin_species

# Return the closest species of the penguin based on the data given.
# In some cases, you may decide that no species is close enough to the data. In that case return "No species found"
#find the inputs through the array on the top 
#within each value of input of array, find through the csv what value it correlates to 

def predict_penguin_species(island, beak_length, beak_height, flipper_length, body_mass, gender):
    closest_species = None
    max_points = 0

    for index in range(len(dataframe)):
        island_value = dataframe["island"][index]
        beak_length_value = dataframe["beak_length_mm"][index]
        beak_height_value = dataframe["beak_height_mm"][index]
        flipper_length_value = dataframe["flipper_length"][index]
        body_mass_value = dataframe["body_mass_g"][index]
        gender_value = dataframe["gender"][index]
        species_value = dataframe["species"][index]

        points = 0

        if island_value == island:
            points += 1
        if gender_value == gender:
            points += 1
        if abs(beak_length_value - float(beak_length)) <= 2:
            points += 1
        if abs(beak_height_value - float(beak_height)) <= 2:
            points += 1
        if abs(flipper_length_value - int(flipper_length)) <= 5:
            points += 1
        if abs(body_mass_value - int(body_mass)) <= 300:
            points += 1

        if points > max_points:
            max_points = points
            closest_species = species_value

    if closest_species:
        return closest_species
    else:
        return "No species found"

    











def main():
    [island, beak_length, beak_height, flipper_length, body_mass, gender] = get_penguin_info()
    species = predict_penguin_species(island, beak_length, beak_height, flipper_length, body_mass, gender)
    print("The species of the penguin is: " + species)

main()