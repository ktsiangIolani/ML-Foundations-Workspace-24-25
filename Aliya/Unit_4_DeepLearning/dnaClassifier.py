# initialize libraries
import pandas as pd
from sklearn.model_selection import train_test_split
#import keras
#from keras import layers
import plotly.express as px
from sklearn.preprocessing import LabelEncoder

# Read in our Data
data = pd.read_csv('classifcation_and_seqs_aln.csv')
#print(data.head())

# Encode our data into numbers
species_encoder = LabelEncoder()

data['species'] = species_encoder.fit_transform(data['species'])

numSpecies = len(set(data['species'].tolist()))
#print("number of species:", numSpecies)

# Encode our sequence into an array of nubers
def convertToNumbers(sequence):
    #returns an array of numbers
    # example: 'ACTG--TG' -> [1, 2, 3, 4, 0, 0, 3, 4]
    base_numbers = {'A': 1, 'C': 2, 'T': 3, 'G': 4} #dictionary with number corresponding base
    encoded_seq = [] #initialise list for encoded sequence
    for base in sequence: #traverse through each base in given sequence
        encoded_seq.append(base_numbers.get(base, 0)) #for that base, append the corresponding number given in dict; or 0 if doesn't exist
    return encoded_seq 

# Add a column to dataframe for encoded sequences
data['encoded_seqs'] = data['sequence'].apply(convertToNumbers)

print(data['encoded_seqs'].iloc[0])
