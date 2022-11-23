import streamlit as st
import pandas as pd


st.write('Hello, *World* :sunglasses:')

image = Image.open('logo.png')

colT1,colT2, colT3 = st.columns([1,8,1])
with colT2:
    st.image(image, width=700)



st.markdown("<h1 style='text-align: center; color: red;'>Seattle Energy Consumption</h1>", unsafe_allow_html=True)


option = st.selectbox(
    'What is your property Use ?',
    ('Low-Rise Multifamily', 'Mixed Use Property', 'Senior Care Community', "University"))


number = st.number_input('Number of floors')
st.write('The current number is ', number)

number2 = st.number_input('Age of the building')
st.write('The current number is ', number2)

number3 = st.number_input('Distance from Seattle Center')
st.write('The current number is ', number3)


if st.button('Predict Consumption'):
    st.write('The building consumption is ')
else:
    st.write('Hit the button')