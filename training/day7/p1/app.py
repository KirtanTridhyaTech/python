import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World!")

df = pd.DataFrame({
    'First Column': [1,2,3,4,5],
    'Second Column': [6, 7, 8, 9, 10]
})

df

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

df = np.random.randn(10, 20)
st.dataframe(df)

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))