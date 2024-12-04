
**Hotel Reservation Cancellation Prediction**

**Overview**

This project aims to predict whether a hotel reservation will be canceled. It leverages machine learning techniques to analyze historical booking data and identify key factors influencing cancellation decisions.

**Data Preprocessing and Exploratory Data Analysis (EDA)**

The dataset was thoroughly cleaned and preprocessed to handle missing values, outliers, and categorical features. EDA techniques were employed to gain insights into the data, including:

* **Data Cleaning:** Removing inconsistencies and errors.
* **Feature Engineering:** Removing features that might be useless.
* **Exploratory Data Analysis:** Visualizing data distributions and relationships.

**Model Development**

A Random Forest Classifier was selected as the primary model for this task. The model was trained on the preprocessed data, with a key modification: **the threshold was set to 0.265 instead of the traditional 0.5**. This adjustment was made to prioritize the prediction of cancellations, even if the model's confidence was relatively low. 

**Model Evaluation**

The model's performance was evaluated using the Area Under the Receiver Operating Characteristic Curve (AUC-ROC). The achieved AUC-ROC score of 0.894 indicates strong predictive power.

**Deployment**

The trained model was deployed as a web application using Flask and Docker. This allows for easy deployment and accessibility.

---

## Links  
- **Docker Image**: [Docker Hub](https://hub.docker.com/repository/docker/mouradadel313/flask_customer_cancellation/tags)

---


### Run with Docker  
Pull the Docker image and start the container:  
```bash  
docker pull mouradadel313/flask_customer_cancellation:latest
docker run -p 5000:5000 mouradadel313/flask_customer_cancellation:latest  
```  
The API will be available at `http://127.0.0.1:5000/`.  

---

## Run with Flask 

### Clone the Repository  
```bash  
https://github.com/Mouradadel1919/Hotel-Reservation-Classification.git
cd Hotel-Reservation-Classification
```  

### Install Requirements  
```bash  
pip install -r requirements.txt  
```  

### Run Flask API  
Start the Flask API locally:  
```bash  
python app.py  
```  
Access the API at `http://127.0.0.1:5000/`.  

