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
def predict_penguin_species(island, beak_length, beak_height, flipper_length, body_mass, gender):
    # Convert string parameters needed as floats
    beak_length = float(beak_length)
    beak_height = float(beak_height)
    flipper_length = float(flipper_length)
    body_mass = float(body_mass)

    high_score = 0
    best_match = "No species found"

    for i in range(1, len(dataframe)): # Loop through each row
        score = 0
        if (dataframe["island"][i] == island):
            score += 1
        if (dataframe["beak_length_mm"][i] > (beak_length - 1) and (dataframe["beak_length_mm"][i] < (beak_length + 1))):
            score += 1
        if (dataframe["beak_height_mm"][i] > (beak_height - 1) and (dataframe["beak_height_mm"][i] < (beak_height + 1))):
            score += 1
        if (dataframe["flipper_length"][i] > (flipper_length - 1) and (dataframe["flipper_length"][i] < (flipper_length + 1))):
            score += 1
        if (dataframe["body_mass_g"][i] > (body_mass - 1) and (dataframe["body_mass_g"][i] < (body_mass + 1))):
            score += 1
        if (dataframe["gender"][i] == gender):
            score += 1
        if score > high_score and score > 2:
            high_score = score
            best_match = dataframe["species"][i]
    return best_match



def main():
    [island, beak_length, beak_height, flipper_length, body_mass, gender] = get_penguin_info()
    species = predict_penguin_species(island, beak_length, beak_height, flipper_length, body_mass, gender)
    print("The species of the penguin is: " + species)

main()