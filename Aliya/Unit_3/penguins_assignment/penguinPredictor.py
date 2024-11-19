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
from sklearn.model_selection import train_test_split
import math

df = pd.read_csv("penguins_train.csv")

# Split dataframe into train and test sets
x = df[['island' ,'beak_length_mm', 'beak_height_mm' ,'flipper_length', 'body_mass_g', 'gender']]
y = df['species']
x_train, x_test, y_train, y_test = train_test_split(x, y) 


#This function take in data about the penguin. It must be entered as island, beak length, beak height, flipper length, body_mass, gender
def get_penguin_info(df_row):
    penguinInfo = df_row.to_list()
    for i in range(1,5):
        penguinInfo[i] = float(penguinInfo[i])
    '''
    while(len(penguinInfo) != 6):
        penguinInfo = input("Enter in data about the penguin you want to identify: ").split(",")

    print("We will now predict the species of the following penguin:" + "\n" + "Island: " + penguinInfo[0] + "\n" + "Beak Length: " + penguinInfo[1] + "\n" + "Beak Height: " + penguinInfo[2] + "\n" + "Flipper Length: " + penguinInfo[3] + "\n" + "Body Mass: " + penguinInfo[4], "Gender: " + penguinInfo[5])
    '''
    return penguinInfo
    


# TODO 1: complete the function predict_penguin_species

# Return the closest species of the penguin based on the data given.
# In some cases, you may decide that no species is close enough to the data. In that case return "No species found"
def predict_penguin_species(island, beak_length, beak_height, flipper_length, body_mass, gender):
    input = [island, beak_length, beak_height, flipper_length, body_mass, gender]
    temp = input

    test = pd.concat([y_test, x_test], axis=1)
    avgs = test.groupby("species")[["beak_length_mm", "beak_height_mm", "flipper_length", "body_mass_g"]].mean()

    
    tested_index = None
    matches = []
    '''
    ind_input = 0
    for measure_type in avgs.columns:
        ind_input += 1
        closest = math.inf
        closest_match = "No species found"
        for species, row in avgs.iterrows():
            if math.isnan(temp[ind_input]):
                temp[ind_input] = 0
            if (abs(avgs[measure_type][species] - temp[ind_input])) < closest:
                closest_match = species
        matches.append(closest_match)

    count = 0
    best_match = matches[0]
    
    for i in matches:
        curr_frequency = matches.count(i)
        if(curr_frequency > count):
            count = curr_frequency
            best_match = i

    print(best_match)'''

    high_score = 0
    best_match = "No species found"
    
    for i in range(len(x_test)): # Loop through each row
        score = 0
        if (x_test.island.iloc[i] == island):
            score += 1
        if abs(x_test.beak_length_mm.iloc[i] - beak_length) < 1:
            score += 1
        if abs(x_test.beak_height_mm.iloc[i] - beak_height) < 1:
            score += 1
        if abs(x_test.flipper_length.iloc[i] - flipper_length) < 1:
            score += 1
        if abs(x_test.body_mass_g.iloc[i] - body_mass) < 1:
            score += 1
        if (x_test.gender.iloc[i] == gender):
            score += 1

        if score > high_score and score > 2:
            high_score = score
            best_match = y_test.iloc[i]
            tested_index = i
    return best_match, tested_index, input


def main():
    accuracy = 0
    results = []
    inputs = []
    matched_info = []
    

    for i in range(len(x_train)):
        [island, beak_length, beak_height, flipper_length, body_mass, gender] = get_penguin_info(x_train.iloc[i])
        species_match, tested_index, input = predict_penguin_species(island, beak_length, beak_height, flipper_length, body_mass, gender)
        results.append(species_match)
        inputs.append(input)
        if tested_index != None:
            matched_info.append(get_penguin_info(x_test.iloc[tested_index]))
        else:
            matched_info.append("Couldn't find a match")
    results = pd.Series(results)
    for i in range(len(results)):
        if (results.iloc[i] == y_train.iloc[i]):
            print("Penguin", i, "species result: ", results.iloc[i])
            #print("Penguin", i, ":", results.iloc[i], "  Actual Species:", y_train.iloc[i], "  Input:", inputs[i], "  Matched Info:", matched_info[i])
            accuracy += 1
        else:
            print("Penguin", i, ":", results.iloc[i], "  Actual Species:", y_train.iloc[i], "  Input:", inputs[i], "  Matched Info:", matched_info[i])
    print("Accuracy:", accuracy, "/", len(results), "correctly identified species")

main()