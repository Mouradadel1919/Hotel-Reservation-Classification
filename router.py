import numpy as np 
import pandas as pd 
import pickle
import joblib

from flask import Flask, render_template, request
model = joblib.load('RF.pkl')

from Utils import *

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/predict", methods= ["GET", "POST"])
def predict():
    if request.method == "POST":
        number_of_adults = int(request.form.get('number_of_adults', 'No option selected in adults'))
        number_of_children    = int(request.form.get('number of children'))
        number_of_weekend_nights  = int(request.form.get('number of weekend nights'))
        number_of_week_nights  = int(request.form.get('number of week nights'))


        type_of_meal    = convert(request.form.get('type of meal'), meal)

        car_parking_space  = int(request.form.get('car parking space'))
        room_type  = convert(request.form.get('room type'), room)
        lead_time = encode_categrical(lead = float(request.form.get('lead time')))

        market_segment_type = convert(request.form.get('market segment type'), market)
        repeated = int(request.form.get('repeated'))
        P_not_C = int(request.form.get('P-not-C'))
        average_price  = encode_categrical(price = float(request.form.get('average price ')))

        special_requests = int(request.form.get('special requests'))
        month = int(request.form.get('month'))
        day = int(request.form.get('day'))
        year = int(request.form.get('year'))


        X_new = pd.DataFrame({'number of adults': [number_of_adults], 'number of children': [number_of_children],
                              'number of weekend nights': [number_of_weekend_nights], 'number of week nights': [number_of_week_nights],
                              'type of meal': [type_of_meal],'car parking space': [car_parking_space], 'room type': [room_type],
                              'lead time': [lead_time], 'market segment type': [market_segment_type], 'repeated': [repeated],'P-not-C': [P_not_C],
                              'average price ': [average_price], 'special requests': [special_requests], 'month': [month], 'day': [day], 
                              'year': [year] 
                              })

        # Call the Function and Preprocess the New Instances
        #X_processed = preprocess_new(X_new)
        y_pred_final = model.predict_proba(X_new.to_numpy().reshape(1, -1))[0][1]
        if y_pred_final <= .265:
            final_pred = "This customer will **not** cancel his Reservation"
        else:
            final_pred = "This customer will cancel his Reservation"



        return render_template('predict.html', y_pred= final_pred)
    else:
        return render_template('predict.html')

    

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



