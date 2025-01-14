# initialize libraries
import pandas as pd
from sklearn.model_selection import train_test_split
import keras
from keras import layers
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
import numpy as np

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

encodedSeqs = []
for seq in data['sequence'].tolist():
    encodedSeqs.append(convertToNumbers(seq))

X = np.array(encodedSeqs)
y = data[['species']]

# Split our data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# Initialise a Neural Network using keras (which comes from tensorflow)
neuralNet = keras.Sequential([
    # define the layers of our network
    layers.Dense(units = 50, activation = 'relu', input_shape = [4795]),
    layers.Dense(units = 50, activation = 'relu'),
    layers.Dense(units = 34),
    ])

# Set up the loss function and backpropagation optimizer
neuralNet.compile(
    loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer = keras.optimizers.Adam(learning_rate=0.01), # the thing that optimises our weights using backprop and gradient descent
    metrics = ['accuracy']
    )

history = neuralNet.fit(
    x_train, y_train,
    validation_data = (x_test, y_test),
    epochs = 29, # number of 'episodes for forward and backprop
    batch_size = 95 # how much data do we do at a time
    )

#df = pd.DataFrame(history.history)['loss']
#px.line(df).update_layout(xaxis_title = 'Epochs', yaxis_title = 'Loss').show()

results = neuralNet.evaluate(x_test, y_test, verbose = 2)

# see what some of our predictions are
predictions = neuralNet.predict(x_test)
for i in range(15):
    predicted = species_encoder.inverse_transform([np.argmax(predictions[i])])[0]
    expected = species_encoder.inverse_transform([y_test.iloc[i]['species']])[0]

    print("predicted: ", predicted, "\nexpected: ", expected)

# Add a column to dataframe for encoded sequences
#data['encoded_seqs'] = data['sequence'].apply(convertToNumbers)

#print(data['encoded_seqs'].iloc[0])