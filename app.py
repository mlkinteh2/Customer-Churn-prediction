import streamlit as st
import joblib
import numpy as np

#loading save model
model = joblib.load("model.pkl")   
scaler = joblib.load("scaler.pkl")  

st.title("Churn Prediction App")
st.divider()
st.write("please enter the values and hit the predict button for getting a prediction")
st.divider()
Tenure = st.number_input("Enter Tenure",min_value = 0,max_value=130, value =10)
age = st.number_input("Enter age",min_value = 10, max_value=100, value=30)
gender = st.selectbox("Enter the Gender",["Male","Female"])
monthlycharge = st.number_input("Enter Monthly charge",min_value=30,max_value = 150)
contracttype = st.selectbox("Select Contract Type", ["Month-to-Month", "One-Year", "Two-Year"])
techsupport = st.selectbox("Tech Support Available?", ["No", "Yes"])



st.divider()
predictbutton = st.button("predict")

st.divider()
if predictbutton:
    gender_selected = 1 if gender == "Female" else 0
    contract_map = {"Month-to-Month": 0, "One-Year": 1, "Two-Year": 2}
    contract_selected = contract_map[contracttype]
    techsupport_selected = 1 if techsupport == "Yes" else 0

    # Keep feature order same as training
    x = [Tenure, age, gender_selected, monthlycharge, contract_selected, techsupport_selected]
    x_array = scaler.transform([x])   # scale input

    prediction = model.predict(x_array)[0]
    predicted = "Yes (Customer will Churn)" if prediction == 1 else "No (Customer will not churn)"
    st.ballons()
    st.write(f"Predicted:{predicted}")
else:
    st.write("please enter the values and use predict button")


   

