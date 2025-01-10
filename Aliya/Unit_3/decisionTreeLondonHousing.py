# Name:
# ML Foundations 24-25
# Supervised Learning - london_house_price_data.csv

# THE GOAL
# This program will take in data about a house in london and predict what species it is

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

# This function take in data about the property. It must be entered as bathrooms, bedrooms, floorAreaSqM, livingRooms, tenure, propertyType, currentEnergyRating, 
# rentEstimate_lowerPrice, rentEstimate_currentPrice, rentEstimate_upperPrice, saleEstimate_lowerPrice, saleEstimate_currentPrice, saleEstimate_upperPrice, 
# saleEstimate_confidenceLevel, saleEstimate_valueChange.numericChange, saleEstimate_valueChange.percentageChange, saleEstimate_valueChange.saleDate, 
# history_date, history_price, history_percentageChange, history_numericChange
def get_property_info():
    propertyInfo = []
    while(len(propertyInfo) != 21):
        propertyInfo = input("Enter in data about the property you want to determine the outcode of: ").split(",")

    print("We will now predict the outcode of the property with the following attributes:" + "\n" + 
          "Bathrooms: " + propertyInfo[0] + "\n" + "Bedrooms: " + propertyInfo[1] + "\n" + "Floor Area SqM: " + propertyInfo[2] + "\n" + "Living Rooms" + propertyInfo[3] + 
          "\n" + "Tenure: " + propertyInfo[4] + "\n" "Property Type: " + propertyInfo[5] + "\n" + "Current Energy Rating: " + propertyInfo[6] + "\n" + 
          "Rent Estimate Lower Price: " + propertyInfo[7] + "\n" + "Rent Estimate Current Price: " + propertyInfo[8] + "\n" + "Rent Estimate Upper Price: " + 
          propertyInfo[9] + "\n" + "Sale Estimate Lower Price" + propertyInfo[10] + "\n" + "Sale Estimate Current Price: " + propertyInfo[11] + "\n" + 
          "Sale Estimate Upper Price: " + propertyInfo[12] + "\n" + "Sale Estimate Confidence Level: " + propertyInfo[13] + "\n" + "Sale Estimate Numeric Value Change: " + 
          propertyInfo[14] + "\n" + "Sale Estimate Percent Value Change: " + propertyInfo[15] + "\n" + "Sale Estimate Value Change Sale Date: " + propertyInfo[16] + "\n" + 
          "History Date: " + propertyInfo[17] + "\n" + "History Price: " + propertyInfo[18] + "\n" + "History Percentage Change: " + propertyInfo[19] + "\n" + 
          "History Numeric Change:" + propertyInfo[20])
    return propertyInfo

#read the data from its csv file
df = pd.read_csv("london_house_price_data.csv", usecols = ['outcode','bathrooms', 'bedrooms', 'floorAreaSqM', 'livingRooms', 'tenure', 'propertyType', 
                                                           'currentEnergyRating', 'rentEstimate_lowerPrice', 'rentEstimate_currentPrice', 'rentEstimate_upperPrice', 
                                                           'saleEstimate_lowerPrice', 'saleEstimate_currentPrice', 'saleEstimate_upperPrice', 'saleEstimate_confidenceLevel', 
                                                           'saleEstimate_valueChange.numericChange', 'saleEstimate_valueChange.percentageChange', 'saleEstimate_valueChange.saleDate', 
                                                           'history_date', 'history_price', 'history_percentageChange', 'history_numericChange'])
df = df.dropna()

# TODO 1: complete the function predict_housing_outcode

# Return the closest outcode of the property based on the data given.
# In some cases, you may decide that no outcode is close enough to the data. In that case return "No outcode found"
def predict_property_outcode(bathrooms, bedrooms, floorAreaSqM, livingRooms, tenure, propertyType, currentEnergyRating, rentEstimate_lowerPrice, rentEstimate_currentPrice, 
                          rentEstimate_upperPrice, saleEstimate_lowerPrice, saleEstimate_currentPrice, saleEstimate_upperPrice, saleEstimate_confidenceLevel, 
                          saleEstimate_valueChange_numeric, saleEstimate_valueChange_percentage, saleEstimate_valueChange_saleDate, history_date, history_price, 
                          history_percentageChange, history_numericChange):
    # Step 1: Preprocess our data - encode our string values into numbers
    # That is outcode, tenure, propertyType, currentEnergyRating, saleEstimate_confidenceLevel, saleEstimate_valueChange.saleDate, history_date 
    outcode_encoder = LabelEncoder()
    tenure_encoder = LabelEncoder()
    propertyType_encoder = LabelEncoder()
    currentEnergyRating_encoder = LabelEncoder()
    saleEstimate_confidenceLevel_encoder = LabelEncoder()
    saleEstimate_valueChange_saleDate_encoder = LabelEncoder()
    history_date_encoder = LabelEncoder()
    # Transform our string values outcode, tenure, propertyType, currentEnergyRating, saleEstimate_confidenceLevel, saleEstimate_valueChange.saleDate, history_date 
    # into a numerical representation like 1, 2, 3, 4
    df['outcode'] = outcode_encoder.fit_transform(df['outcode'])
    df['tenure'] = tenure_encoder.fit_transform(df['tenure'])
    df['propertyType'] = propertyType_encoder.fit_transform(df['propertyType'])
    df['currentEnergyRating'] = currentEnergyRating_encoder.fit_transform(df['currentEnergyRating'])
    df['saleEstimate_confidenceLevel'] = saleEstimate_confidenceLevel_encoder.fit_transform(df['saleEstimate_confidenceLevel'])
    df['saleEstimate_valueChange.saleDate'] = saleEstimate_valueChange_saleDate_encoder.fit_transform(df['saleEstimate_valueChange.saleDate'])
    df['history_date'] = history_date_encoder.fit_transform(df['history_date'])

    # Step 1.5: choose a subset of traits using a corrolation heatmap
    corr_matrix = df.corr()
    #print(corr_matrix)

    #px.imshow(corr_matrix, text_auto = True, range_color = [-1, 1], color_continuous_scale = 'RdBu').show()

    # Step 2: Select the features we want to use to train out data
    # Removed: 'rentEstimate_lowerPrice' (0.685828813958972 --> 0.6858759726479604)
    # 'saleEstimate_lowerPrice', (0.6858759726479604 --> 0.6826220231077577)
    # 'tenure', (0.6858759726479604 --> 0.6732374439990568)
    # 
    X = df[['bathrooms', 'bedrooms', 'floorAreaSqM', 'livingRooms', 'tenure', 'propertyType', 'currentEnergyRating', 'rentEstimate_currentPrice', 
            'rentEstimate_upperPrice', 'saleEstimate_lowerPrice', 'saleEstimate_currentPrice', 'saleEstimate_upperPrice', 'saleEstimate_confidenceLevel', 
            'saleEstimate_valueChange.numericChange', 'saleEstimate_valueChange.percentageChange', 'saleEstimate_valueChange.saleDate', 'history_date', 'history_price', 
            'history_percentageChange', 'history_numericChange']]

    # Step 3: Select the features we want to predict
    y = df['outcode']

    # Step 4: Train our decision tree model
    model = DecisionTreeClassifier(random_state=1)
    model.fit(X, y)

    #print(export_text(model, feature_names = list(X.columns)))

    # Step 5: Use our model to predict the outcode of our property
    single_property = pd.DataFrame({
        "bathrooms": [bathrooms], 
        "bedrooms" : [bedrooms], 
        "floorAreaSqM": [floorAreaSqM], 
        "livingRooms": [livingRooms], 
        "tenure": tenure_encoder.transform([tenure]), 
        "propertyType": propertyType_encoder.transform([propertyType]),
        "currentEnergyRating": currentEnergyRating_encoder.transform([currentEnergyRating]),
        #"rentEstimate_lowerPrice": [rentEstimate_lowerPrice], 
        "rentEstimate_currentPrice": [rentEstimate_currentPrice], 
        "rentEstimate_upperPrice": [rentEstimate_upperPrice], 
        "saleEstimate_lowerPrice": [saleEstimate_lowerPrice], 
        "saleEstimate_currentPrice": [saleEstimate_currentPrice], 
        "saleEstimate_upperPrice": [saleEstimate_upperPrice], 
        "saleEstimate_confidenceLevel": saleEstimate_confidenceLevel_encoder.transform([saleEstimate_confidenceLevel]),
        "saleEstimate_valueChange.numericChange": [saleEstimate_valueChange_numeric], 
        "saleEstimate_valueChange.percentageChange": [saleEstimate_valueChange_percentage], 
        "saleEstimate_valueChange.saleDate": saleEstimate_valueChange_saleDate_encoder.transform([saleEstimate_valueChange_saleDate]),
        "history_date": history_date_encoder.transform([history_date]),
        "history_price": [history_price], 
        "history_percentageChange": [history_percentageChange], 
        "history_numericChange": [history_numericChange]
    })

    outcode = model.predict(single_property)[0]
    outcode = outcode_encoder.inverse_transform([int(outcode)])[0]

    # Step 6: Let's see how well our model is doing by computing an accuracy rate
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    # retraining out model using 80 percent of the data
    model.fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    print("Accuracy: ", accuracy)
    return outcode

def main():
    [bathrooms, bedrooms, floorAreaSqM, livingRooms, tenure, propertyType, currentEnergyRating, rentEstimate_lowerPrice, rentEstimate_currentPrice, 
     rentEstimate_upperPrice, saleEstimate_lowerPrice, saleEstimate_currentPrice, saleEstimate_upperPrice, saleEstimate_confidenceLevel, saleEstimate_valueChange_numeric, 
     saleEstimate_valueChange_percentage, saleEstimate_valueChange_saleDate, history_date, history_price, history_percentageChange, history_numericChange] = get_property_info()
    outcode = predict_property_outcode(bathrooms, bedrooms, floorAreaSqM, livingRooms, tenure, propertyType, currentEnergyRating, rentEstimate_lowerPrice, rentEstimate_currentPrice, rentEstimate_upperPrice, saleEstimate_lowerPrice, saleEstimate_currentPrice, saleEstimate_upperPrice, saleEstimate_confidenceLevel, saleEstimate_valueChange_numeric, saleEstimate_valueChange_percentage, saleEstimate_valueChange_saleDate, history_date, history_price, history_percentageChange, history_numericChange)
    print("The outcode of the property is: " + outcode)

main()


# 2.0,2.0,73.0,1.0,Leasehold,Purpose Built Flat,D,2800.0,3000.0,3250.0,619000.0,651000.0,684000.0,HIGH,28000.0,4.49438202247191,2023-10-31,2023-10-31,623000,3.833333333333333,23000.0
# 1.0,2.0,75.0,1.0,Freehold,Mid Terrace House,D,2100.0,2350.0,2550.0,557000.0,587000.0,616000.0,HIGH,87000.0,17.4,2021-04-09,2021-04-09,500000,5.485232067510549,26000.0