import streamlit as st
import pandas as pd
from PIL import Image
import pickle


st.write('Hello, *World* :sunglasses:')

image = Image.open('logo.png')

colT1,colT2, colT3 = st.columns([1,8,1])
with colT2:
    st.image(image, width=700)



st.markdown("<h1 style='text-align: center; color: blue;'>CO2 Emissions Predictions</h1>", unsafe_allow_html=True)

# # welcome info
    st.info(":high_brightness: Welcome here !  caracteristiques batiments")


option = st.selectbox(
    'What is your property Use ?',
    ('Low-Rise Multifamily', 'Mixed Use Property', 'Senior Care Community', "University"))


number = st.number_input('Number of floors')
st.write('The current number is ', number)

number2 = st.number_input('Age of the building')
st.write('The current number is ', number2)

number3 = st.number_input('Distance from Seattle Center')
st.write('The current number is ', number3)

# # welcome info
    st.info(":high_brightness: Welcome here !  Hop,  you can predict the energy use by the building in Seattle and the GHG emissions by year")

number4 = st.number_input('NaturalGas(kBtu)')
st.write('The current number is ', number4)

number5 = st.number_input('SteamUse(kBtu)')
st.write('The current number is ', number5)

number6 = st.number_input('GHGEmissionsIntensity')
st.write('The current number is ', number6)

number7 = st.number_input('SourceEUI(kBtu/sf)')
st.write('The current number is ', number7)

        
    with open('rf_app_pickle' , 'rb') as f:
        model= pickle.load(f)


if st.button('Predict Consumption'):
    st.write('The building consumption is ')
else:
    st.write('Hit the button')