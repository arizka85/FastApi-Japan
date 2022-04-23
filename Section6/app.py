import streamlit as st
import pandas as pd
import numpy as np

st.button("Click me")

if st.button("Test !"):
    st.write("Hello Test")



st.checkbox("Checkbox 1")




options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
st.write('You selected:', options)












# streamlit run app.py

