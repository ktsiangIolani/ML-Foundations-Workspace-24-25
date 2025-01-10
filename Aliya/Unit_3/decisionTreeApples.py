# Name:
# ML Foundations 24-25
# Supervised Learning - apple_quality.csv

# THE GOAL
# This program will take in data about an apple and predict what its quality is


#import necessary python tools
import pandas as pd
# DecisionTreeClassifier is the model we are using
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
import plotly.express as px
from sklearn.model_selection import train_test_split

#This function take in data about the apple. It must be entered as size, weight, sweetness, crunchiness, juiciness, ripeness, acidity
def get_apple_info():
    appleInfo = []
    while(len(appleInfo) != 7):
        appleInfo = input("Enter in data about the penguin you want to identify: ").split(",")

    print("We will now predict the quality of the apple with the following attributes:" + "\n" + "Size: " + appleInfo[0] + "\n" + "Weight: " + appleInfo[1] + "\n" + "Sweetness: " + appleInfo[2] + "\n" + "Crunchiness" + appleInfo[3] + "\n" + "Juiciness: " + appleInfo[4], "Ripeness: " + appleInfo[5] + "\n" + "Acidity: " + appleInfo[6])
    return appleInfo

#read the data from its csv file
df = pd.read_csv("apple_quality.csv")
df = df.dropna()

# TODO 1: complete the function predict_apple_quality

# Return the closest quality of the apple based on the data given.
# In some cases, you may decide that no quality is close enough to the data. In that case return "No quality found"
def predict_apple_quality(size, weight, sweetness, crunchiness, juiciness, ripeness, acidity):
    # Step 1: Preprocess our data - encode our string values into numbers
    # That is quality
    quality_encoder = LabelEncoder()
    # Transform our string value quality into a numerical representation like 1 and 2
    df['Quality'] = quality_encoder.fit_transform(df['Quality'])

    # Step 1.5: choose a subset of traits using a corrolation heatmap
    corr_matrix = df.corr()
    #print(corr_matrix)

    #px.imshow(corr_matrix, text_auto = True, range_color = [-1, 1], color_continuous_scale = 'RdBu').show()

    # Step 2: Select the features we want to use to train out data
    # Removed acidity 0.76375 --> 0.76875
    # Removed acidity and ripeness 0.76875 --> 0.7325
    # Removed acidity and crunchiness  0.76875 --> 0.7675
    # Final: Removing only acidity
    X = df[['Size', 'Weight', 'Sweetness', 'Crunchiness', 'Juiciness', 'Ripeness']]

    # Step 3: Select the features we want to predict
    y = df['Quality']

    # Step 4: Train our decision tree model
    model = DecisionTreeClassifier(random_state=1)
    model.fit(X, y)

    print(export_text(model, feature_names = list(X.columns)))

    # Step 5: Use our model to predict the quality of our apple
    single_apple = pd.DataFrame({
        "Size": [size],
        "Weight": [weight],
        "Sweetness": [sweetness],
        "Crunchiness": [crunchiness],
        "Juiciness": [juiciness],
        "Ripeness": [ripeness],
        #"Acidity": [acidity],
    })

    quality = model.predict(single_apple)[0]
    quality = quality_encoder.inverse_transform([int(quality)])[0]

    # Step 6: Let's see how well our model is doing by computing an accuracy rate
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    # retraining out model using 80 percent of the data
    model.fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    print("Accuracy: ", accuracy)
    return quality

def main():
    [size, weight, sweetness, crunchiness, juiciness, ripeness, acidity] = get_apple_info()
    quality = predict_apple_quality(size, weight, sweetness, crunchiness, juiciness, ripeness, acidity)
    print("The quality of the apple is: " + quality)

main()
