#initialise libraries

import pandas as pd
from sklearn.model_selection import train_test_split

# Read in our Data
data = pd.read_csv("red-wine.csv")
print(data.head())

# Define our features and target
X = data[["fixed acidity", "volatile acidity", "citric acid","residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol"]]
Y = data[["quality"]]

# Split our data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# Initialise a Neural Network using keras (which comes from tensorflow)

