#initialise libraries

import pandas as pd
from sklearn.model_selection import train_test_split
import keras
from keras import layers
import plotly.express as px

# Read in our Data
data = pd.read_csv('red-wine.csv')
#print(data.head())

# Define our features and target
X = data[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']]
y = data[['quality']]

# Split our data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# Initialise a Neural Network using keras (which comes from tensorflow)
neuralNet = keras.Sequential([
    # define the layers of our network
    layers.Dense(units = 5, activation = 'relu', input_shape = [11]),
    layers.Dense(units = 4, activation = 'relu'),
    layers.Dense(units = 1)
    ])

# Set up the loss function and backpropagation optimizer
neuralNet.compile(
    loss = 'mse',
    optimizer = 'adam' # the thing that optimises our weights using backprop and gradient descent
    )

history = neuralNet.fit(
    x_train, y_train,
    validation_data = (x_test, y_test),
    epochs = 25, # number of 'episodes for forward and backprop
    batch_size = 700 # how much data do we do at a time
    )

df = pd.DataFrame(history.history)['loss']
px.line(df).update_layout(xaxis_title = 'Epochs', yaxis_title = 'Loss').show()