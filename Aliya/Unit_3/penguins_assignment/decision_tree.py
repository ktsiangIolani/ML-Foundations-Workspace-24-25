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
# DecisionTreeClassifier is the model we are using
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
import plotly.express as px
from sklearn.model_selection import train_test_split

#This function take in data about the penguin. It must be entered as island, beak length, beak height, flipper length, body_mass, gender
def get_penguin_info():
    penguinInfo = []
    while(len(penguinInfo) != 6):
        penguinInfo = input("Enter in data about the penguin you want to identify: ").split(",")

    print("We will now predict the species of the following penguin:" + "\n" + "Island: " + penguinInfo[0] + "\n" + "Beak Length: " + penguinInfo[1] + "\n" + "Beak Height: " + penguinInfo[2] + "\n" + "Flipper Length: " + penguinInfo[3] + "\n" + "Body Mass: " + penguinInfo[4], "Gender: " + penguinInfo[5])
    return penguinInfo

#read the data from its csv file
df = pd.read_csv("penguins_train.csv")
df = df.dropna()

# TODO 1: complete the function predict_penguin_species

# Return the closest species of the penguin based on the data given.
# In some cases, you may decide that no species is close enough to the data. In that case return "No species found"
def predict_penguin_species(island, beak_length, beak_height, flipper_length, body_mass, gender):
    # Step 1: Preprocess our data - encode our string values into numbers
    # That is island, gender and species
    species_encoder = LabelEncoder()
    gender_encoder = LabelEncoder()
    island_encoder = LabelEncoder()
    # Transform our string values gender, species and islands into a numerical representation like 1, 2, 3, 4
    df['species'] = species_encoder.fit_transform(df['species'])
    df['gender'] = gender_encoder.fit_transform(df['gender'])
    df['island'] = island_encoder.fit_transform(df['island'])

    # Step 1.5: choose a subset of traits using a corrolation heatmap
    corr_matrix = df.corr()
    print(corr_matrix)

    #px.imshow(corr_matrix, text_auto = True, range_color = [-1, 1], color_continuous_scale = 'RdBu').show()

    # Step 2: Select the features we want to use to train out data
    # Removing body_mass_g because of redundancy - high correlation with flipper_length, and lower correlation with species comapred to flipper_length's
    X = df[['island' , 'beak_length_mm','flipper_length', 'gender']]

    # Step 3: Select the features we want to predict
    y = df['species']

    # Step 4: Train our decision tree model
    model = DecisionTreeClassifier(random_state=1)
    model.fit(X, y)

    print(export_text(model, feature_names = list(X.columns)))

    # Step 5: Use our model to predict the species of our penguin
    single_penguin = pd.DataFrame({
        "island": island_encoder.transform([island]),
        "beak_length_mm": [beak_length],
        #"beak_height_mm": [beak_height],
        "flipper_length": [flipper_length],
        #"body_mass_g": [body_mass],
        "gender": gender_encoder.transform([gender]),
    })

    species = model.predict(single_penguin)[0]
    species = species_encoder.inverse_transform([int(species)])[0]

    # Step 6: Let's see how well our model is doing by computing an accuracy rate
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    # retraining out model using 80 percent of the data
    model.fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    print("Accuracy: ", accuracy)
    return species

def main():
    [island, beak_length, beak_height, flipper_length, body_mass, gender] = get_penguin_info()
    species = predict_penguin_species(island, beak_length, beak_height, flipper_length, body_mass, gender)
    print("The species of the penguin is: " + species)

main()



