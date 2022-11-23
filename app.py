import streamlit as st
import pandas as pd


st.write('Hello, *World* :sunglasses:')


st.markdown("<h1 style='text-align: center; color: red;'>Seattle energy</h1>", unsafe_allow_html=True)


option = st.selectbox(
    'What is your property Use ?',
    ('Low-Rise Multifamily', 'Mixed Use Property', 'Senior Care Community', "University"))


