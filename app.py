# ---------------- IMPORT LIBRARIES ----------------
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# ---------------- TITLE ----------------
st.title("🚗 Car Price Prediction")

# ---------------- LOAD DATA ----------------
# Make sure car_data.csv is in same folder
data = pd.read_csv("car_data.csv")

# ---------------- PREPROCESS ----------------
data['Fuel_Type'] = data['Fuel_Type'].map({'Petrol': 2, 'Diesel': 1, 'CNG': 0})
data['Seller_Type'] = data['Seller_Type'].map({'Dealer': 0, 'Individual': 1})
data['Transmission'] = data['Transmission'].map({'Manual': 1, 'Automatic': 0})

# Feature Engineering
data['Car_Age'] = 2025 - data['Year']

# Drop unused columns
data = data.drop(['Car_Name', 'Year'], axis=1)

# ---------------- TRAIN MODEL ----------------
X = data.drop('Selling_Price', axis=1)
y = data['Selling_Price']

model = RandomForestRegressor()
model.fit(X, y)

# ---------------- USER INPUT ----------------
st.subheader("Enter Car Details")

year = st.slider("Year", 2000, 2025, 2015)
present_price = st.number_input("Present Price (Lakhs)", 0.0, 50.0, 5.0)
kms = st.number_input("Kms Driven", 0, 300000, 50000)

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller = st.selectbox("Seller Type", ["Dealer", "Individual"])
trans = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner", [0,1,2,3])

# ---------------- ENCODING ----------------
fuel_map = {"Petrol":2,"Diesel":1,"CNG":0}
seller_map = {"Dealer":0,"Individual":1}
trans_map = {"Manual":1,"Automatic":0}

car_age = 2025 - year

input_data = np.array([[present_price, kms,
                        fuel_map[fuel],
                        seller_map[seller],
                        trans_map[trans],
                        owner,
                        car_age]])

# ---------------- PREDICTION ----------------
if st.button("Predict Price"):
    result = model.predict(input_data)
    st.success(f"💰 Estimated Price: ₹ {round(result[0], 2)} Lakhs")
