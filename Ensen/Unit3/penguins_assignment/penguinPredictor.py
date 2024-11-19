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
import plotly.express as px

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
def predict_penguin_species(island, beak_length, beak_height, flipper_length, body_mass, gender):
    max_point = 0

    for i in range(len(dataframe)):
        current_point = 0
        species_name = dataframe["species"][i]
        island_name = dataframe["island"][i]
        if island_name == island:
            current_point += 1
        beak_length_num = dataframe["beak_length_mm"][i]
        if abs(beak_length_num - float(beak_length)) <= 4:
            current_point += 1
        beak_height_num = dataframe["beak_height_mm"][i]
        if abs(beak_height_num - float(beak_height)) <= 4:
            current_point += 1
        flipper_length_num = dataframe["flipper_length"][i]
        if abs(flipper_length_num - int(flipper_length)) <= 8:
            current_point += 1
        body_mass_num = dataframe["body_mass_g"][i]
        if abs(body_mass_num - int(body_mass)) <= 350:
            current_point += 1
        gender_name = dataframe["gender"][i]
        if gender_name == gender:
            current_point += 1
        
        if current_point > max_point:
            max_point = current_point
            closest_species = species_name
    
    
    if closest_species == closest_species:
        return closest_species
    else: 
        return "No species found"


def main():
    #px.scatter(dataframe, x = "flipper_length", y = "beak_length_mm", color = "species", symbol = "island").show()
    [island, beak_length, beak_height, flipper_length, body_mass, gender] = get_penguin_info()
    species = predict_penguin_species(island, beak_length, beak_height, flipper_length, body_mass, gender)
    print("The species of the penguin is: " + species)

main()

