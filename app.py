# ---------------- IMPORT LIBRARIES ----------------
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(page_title="Car Price Prediction", layout="centered")

st.title("🚗 Car Price Prediction App")
st.write("Predict the resale value of your car instantly")

# ---------------- LOAD DATA ----------------
try:
    data = pd.read_csv("car_data.csv")
except:
    st.error("❌ car_data.csv file not found!")
    st.stop()

# ---------------- PREPROCESS DATA ----------------
data['Fuel_Type'] = data['Fuel_Type'].map({'Petrol': 2, 'Diesel': 1, 'CNG': 0})
data['Seller_Type'] = data['Seller_Type'].map({'Dealer': 0, 'Individual': 1})
data['Transmission'] = data['Transmission'].map({'Manual': 1, 'Automatic': 0})

# Create new feature
data['Car_Age'] = 2025 - data['Year']

# Drop unused columns
data = data.drop(['Car_Name', 'Year'], axis=1)

# ---------------- TRAIN MODEL ----------------
X = data.drop('Selling_Price', axis=1)
y = data['Selling_Price']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# ---------------- USER INPUT ----------------
st.subheader("Enter Car Details")

year = st.slider("Year of Purchase", 2000, 2025, 2015)
present_price = st.number_input("Present Price (Lakhs)", 0.0, 50.0, 5.0)
kms_driven = st.number_input("Kilometers Driven", 0, 300000, 50000)

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Number of Owners", [0, 1, 2, 3])

# ---------------- ENCODING INPUT ----------------
fuel_map = {"Petrol": 2, "Diesel": 1, "CNG": 0}
seller_map = {"Dealer": 0, "Individual": 1}
trans_map = {"Manual": 1, "Automatic": 0}

car_age = 2025 - year

input_data = np.array([[present_price,
                        kms_driven,
                        fuel_map[fuel],
                        seller_map[seller],
                        trans_map[transmission],
                        owner,
                        car_age]])

# ---------------- PREDICTION ----------------
if st.button("Predict Price"):
    try:
        prediction = model.predict(input_data)
        st.success(f"💰 Estimated Price: ₹ {round(prediction[0], 2)} Lakhs")
    except Exception as e:
        st.error("❌ Prediction failed")
        st.write(e)

# ---------------- FOOTER ----------------
st.markdown("---")
st.write("Built with ❤️ using Streamlit")
