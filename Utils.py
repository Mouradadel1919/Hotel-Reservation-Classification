import numpy as np 
import pandas as pd
import pickle

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


# IQR Function with quantiles (25, 75) 
def IQR(column_name, df):
    IQR = 0
    
    q1 = df[column_name].quantile(.25)
    q3 = df[column_name].quantile(.75)
    
    IQR= q3 - q1
    
    lower= q1 - 1.5 * IQR
    upper= q3 + 1.5 * IQR
    
    df.drop(df[((df[column_name] > upper) | (df[column_name] < lower))].index, inplace= True, axis=0)



data = pd.read_csv(open("Customer_Cancelation.csv","r"))
data.drop(columns= ["Booking_ID"], axis= 1, inplace= True)

data[['month', 'day', 'year']] = data["date of reservation"].str.split("/", expand = True)

# we will delete the remaining 37 instance with "-" to have the same number of rows of data
data.drop(data[data["day"].isna()].index,
             axis= 0, 
             inplace= True,
             )
data.drop(columns="date of reservation", inplace=True)

#Re-Format
data["month"]= data["month"].astype("int64")
data["day"]= data["day"].astype("int64")
data["year"]= data["year"].astype("int64")
data["lead time"]= data["lead time"].astype("float64")


# Custom Encoding for Specific Values
meal = {
    "Not Selected" : 0,
    "Meal Plan 1": 1,
    "Meal Plan 2": 2,
    "Meal Plan 3": 3
    
}

# Custom Encoding for Specific Values
room = {
    "Room_Type 1": 1,
    "Room_Type 2": 2,
    "Room_Type 3": 3,
    "Room_Type 4": 4,
    "Room_Type 5": 5,
    "Room_Type 6": 6,
    "Room_Type 7": 7,
    
}

market = {
    "Offline": 0,
    "Online": 1,
    "Corporate": 2,
    "Aviation": 3,
    "Complementary": 4
    
}



# Custom Encoding for Specific Values
booking = {
    "Not_Canceled" : 0,
    "Canceled": 1
}
data["booking status"] = data["booking status"].map(booking)


features = data.loc[:,~data.columns.isin(["booking status"])]
con_features = data.loc[:, data.columns.isin(['lead time', 'average price '])]
disc_features = data.loc[:, ~data.columns.isin(['lead time', 'average price ', 'booking status'])]



for col in data.loc[:,con_features.columns].columns.to_list():
    IQR(col, data)

data.reset_index(inplace=True, drop= True)



features = data.loc[:,~data.columns.isin(["booking status",  "P-C"])]
target = data.loc[:, ["booking status"]]

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=.2, random_state=42)

scaler =  StandardScaler()
scaler.fit(X_train[con_features.columns])

def encode_categrical(lead = 0, price = 0):
    if (lead != 0) & (price == 0):
        return scaler.transform([[lead , price]])[0][0]
    elif (lead == 0) & (price != 0):
        return scaler.transform([[lead , price]])[0][1]
    else:
        pass

def convert(item, map_dict):
    return map_dict.get(item)
