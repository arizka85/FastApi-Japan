import streamlit as st
import pandas as pd

st.write("Sample App")


df = pd.DataFrame({
    "satu": [1, 2, 3, 4],
    "dua": [-1, -2, -3, -4]
})

st.dataframe(df)


st.json(
{
    'data': {
        'name': 'abc',
        'age': 123
    }
}

)


# streamlit run app.py

