import streamlit as st
import pandas as pd
import pickle
import numpy as np

model = pickle.load(open("Car_Price_Predictor/Car_price_predictor_Model.pkl",'rb'))
 
df = pd.read_csv(r"C:\Users\anas1\OneDrive\Desktop\ML\Car_Price_Predictor\Cleaned_car.csv")

st.title("Car Price Predictor")
st.text("")

car_brand = st.selectbox(
    "Select Car Brand",
    sorted(df['company'].unique()),
    index=None,
    placeholder="Select Car...",
)

filtered_models = df[df['company'] == car_brand]['name'].unique()

st.text("")
car_model = st.selectbox(
    "Select Car Model",
    sorted(filtered_models),
    index=None,
    placeholder="Select Car Model...",
)

st.text("")
year = st.slider("Select Year", 1995,2010,2020)
st.text("")
kms = st.number_input("Insert KMS Driven", value=None, placeholder="Type a number...")

st.text("")
fuel = st.radio(label="Type Of Fuel",options=df['fuel_type'].unique())


if 'prediction' not in st.session_state:
    st.session_state.prediction = None

if st.button(label="Predict"):
    
    input_data = pd.DataFrame([[car_model, car_brand, year, kms, fuel]], 
                               columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])

    prediction = model.predict(input_data)
    rounded_prediction = round(prediction[0], 2)

    st.markdown(f"### Predicted Car Price : ₹ {rounded_prediction:.2f}")


