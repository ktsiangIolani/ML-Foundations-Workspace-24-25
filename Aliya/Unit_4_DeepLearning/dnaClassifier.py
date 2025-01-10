# initialize libraries
import pandas as pd
from sklearn.model_selection import train_test_split
import keras
from keras import layers
import plotly.express as px
from sklearn.preprocessing import LabelEncoder

# Read in our Data
data = pd.read_csv('classifcation_and_seqs_aln.csv')
print(data.head())

# Encode our data into numbers
species_encoder = LabelEncoder()

data['species'] = species_encoder.fit_transform(df['species'])

numSpecies = len(set(data['species'].tolist()))
print("number of species:", numSpecies)

# Encode our sequence into an array of nubers
def convertToNumbers(sequence):
    #returns an array of numbers
    # example: 'ACTG--TG' -> [1, 2, 3, 4, 0, 0, 3, 4]