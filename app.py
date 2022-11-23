import streamlit as st
import pandas as pd


st.write('Hello, *World* :sunglasses:')


st.markdown("<h1 style='text-align: center; color: red;'>Seattle energy</h1>", unsafe_allow_html=True)


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