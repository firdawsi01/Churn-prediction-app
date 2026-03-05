import streamlit as st
import joblib
import numpy as np

model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")

income = st.number_input("Income Level")
transactions = st.number_input("Amount Spent")
app_usage = st.number_input("App Usage Frequency")

if st.button("Predict Churn"):
    data = np.array([[income, transactions, app_usage]])
    prediction = model.predict(data)
    
    if prediction == 1:
        st.error("Customer likely to churn")
    else:
        st.success("Customer likely to stay")
    