import pandas as pd
# DecisionTreeClassifier is the model we are using
from sklearn.tree import DecisionTreeClassifier, export_text


#This function take in data about the penguin. It must be entered as island, beak length, beak height, flipper length, body_mass, gender
def get_penguin_Info():
    penguinInfo = []
    while(len(penguinInfo) != 6):
        penguinInfo = input("Enter in data about the penguin you want to identify: ").split(",")

    print("We will now predict the species of the following penguin:" + "\n" + "Island: " + penguinInfo[0] + "\n" + "Beak Length: " + penguinInfo[1] + "\n" + "Beak Height: " + penguinInfo[2] + "\n" + "Flipper Length: " + penguinInfo[3] + "\n" + "Body Mass: " + penguinInfo[4], "Gender: " + penguinInfo[5])
    return penguinInfo

# Read in the data from its csv file
df = pd.read_csv("penguins_train.csv")
# Removes NA values from the dataframe
df = df.dropna()


# Predict our penguin species using the Decision Tree Model from Scikit-learn
def predict_penguin_species(island, beak_length, beak_height, flipper_length, body_mass, gender):
    # Step 1: Preprocess our data - encode our string values into numbers
    # That is island, gender and species
    species_encoder = LabelEncoder()
    df["species"] = species_encoder.fit_transform(df["species"])
    


def main():
    [island, beak_length, beak_height, flipper_length, body_mass, gender] = get_penguin_Info()
    species = predict_penguin_species(island, beak_length, beak_height, flipper_length, body_mass, gender)
    print("The species of the penguin is:" + species)

main()


