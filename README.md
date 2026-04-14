Car Price Prediction 🚗

This project is a Machine Learning web application that predicts the resale price of used cars based on user input. The model is trained dynamically inside the application using the dataset, making it simple and easy to deploy without saving a separate model file.

Project Overview

The application uses a dataset of used cars to train a regression model and predict the selling price. Users can input details such as year, fuel type, kilometers driven, and ownership to get an estimated price instantly.

Technologies Used

Python
Pandas
NumPy
Scikit-learn
Streamlit

Features

Predict car resale price instantly
No need for a saved model file (model trains inside the app)
Simple and interactive user interface
Fast and accurate predictions
Easy deployment

Project Structure

app.py → Streamlit web application (includes training + prediction)
car_data.csv → Dataset used for training
requirements.txt → Required libraries

How to Run the Project

Step 1: Install required libraries
pip install -r requirements.txt

Step 2: Run the Streamlit app
streamlit run app.py

The application will open in your browser automatically.

How It Works

The dataset is loaded from a CSV file.
Categorical values such as fuel type and transmission are converted into numerical format.
A new feature called Car Age is created from the year of purchase.
A Random Forest Regressor model is trained using the dataset.
The trained model predicts the car price based on user inputs.

Deployment

Upload all project files to GitHub.
Connect the repository to Streamlit Cloud.
Select app.py as the main file.
Deploy the application.

Advantages

No model.pkl file required
Easy for beginners
No file loading errors
Works directly after deployment

Future Improvements

Add better UI design
Include data visualization and graphs
Improve model accuracy with advanced algorithms
Add more features for prediction

Developed By

Siddu Shirol
