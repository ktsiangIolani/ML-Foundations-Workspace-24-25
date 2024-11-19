# Name: Ethan Mashimo
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
    # using the penguins_train.csv compare using the given data to determine what penguin it is
    # if given data is similar in multiple aspects of the csv, maybe return a similarity score of some sort
    beak_length = float(beak_length)
    beak_height = float(beak_height)
    flipper_length = float(flipper_length)
    body_mass = float(body_mass)
    
    # Initialize scores
    scores = [0, 0, 0]
    
    # Scoring based on beak length
    if 32 <= beak_length <= 44:
        scores[0] += 2
    if 40 <= beak_length <= 58:
        scores[1] += 2
    if 42 <= beak_length <= 57:
        scores[2] += 3

    # Scoring based on flipper length
    if 170 <= flipper_length <= 210:
        scores[0] += 3
        scores[1] += 2
    if 203 <= flipper_length <= 231:
        scores[2] += 4

    # Scoring based on weight
    if gender == "male":
        if 3700 <= body_mass <= 4775:
            scores[0] += 2
        if 3700 <= body_mass <= 4800:
            scores[1] += 2
        if 4500 <= body_mass <= 6300:
            scores[2] += 4
    elif gender == "female":
        if 2700 <= body_mass <= 4000:
            scores[0] += 2
        if 2700 <= body_mass <= 4200:
            scores[1] += 2
        if 3950 <= body_mass <= 5100:
            scores[2] += 4

    # Scoring based on island 
    if island == "Torgersen":
        scores[0] += 12
    if island == "Biscoe":
        scores[2] += 4
    if island == "Dream":
        scores[1] += 8
        scores[0] += 6
    
    print(scores[0])
    print(scores[1])
    print(scores[2])
    
    max_score = max(scores)

    if max_score == 0:
        return "No species found"
    
    species_list = ["Adelie", "Chinstrap", "Gentoo"]
    

    return species_list[scores.index(max_score)]









def main():
    [island, beak_length, beak_height, flipper_length, body_mass, gender] = get_penguin_info()
    species = predict_penguin_species(island, beak_length, beak_height, flipper_length, body_mass, gender)
    print("The species of the penguin is: " + species)

main()