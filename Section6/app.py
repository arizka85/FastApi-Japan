import streamlit as st
import pandas as pd
import numpy as np

st.write("Sample App")


st.write(np.random.rand(20, 3))



df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']

)
# st.line_chart(df)
# st.area_chart(df)
st.bar_chart(df)




# streamlit run app.py

