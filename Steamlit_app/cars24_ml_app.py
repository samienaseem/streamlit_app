import pickle 
import pandas as pd
import streamlit as st
import datetime


cars_df=pd.read_csv('cars24-car-price.csv')

st.write(""" ## Cars24 used car price prediction """)

st.dataframe(cars_df)

col1,col2=st.columns(2)

encode_dict={
    "fuel_type":{'Diesel':1, 'Petrol':2, 'CNG':3, 'LPG':4, 'Electric':5},
    "transmission_type":{'Manual':1, 'Automatic': 2},
    "seller_type": {"Dealer": 1, "Individual": 2, "Trustmark Dealer":3}
}

def model_pred(fuel_type,transmission_type, engine, seats):
    with open("car_pred",'rb') as file:
        reg_model=pickle.load(file)

    input_feature=[[2018.0, 1, 40000, fuel_type, transmission_type, 19.70, engine, 86.30, seats]]
    return reg_model.predict(input_feature)

with col1:
    fuel_type=col1.selectbox("Select fuel type", ['Diesel','Petrol', 'CNG', 'LPG', 'Electric'])

    engine=col1.slider("Set the engine power", 500,5000,step=100)

with col2:
   transmission_type = col2.selectbox("select the transmission type", ['Automatic','Manual'])
   seats=col2.selectbox("No of Seats", [2,4,5,6,7])


if(st.button("Predict price")):
    fuel_type = encode_dict['fuel_type'][fuel_type]
    transmission_type = encode_dict['transmission_type'][transmission_type]

    price = model_pred(fuel_type, transmission_type, engine, seats)
    st.text("Predicted price of the car: "+ str(price))
    # st.text(encode_dict['fuel_type'][fuel_type])




