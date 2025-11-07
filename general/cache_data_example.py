# st.cache_data automatically reloads (recomputes) whenever any input argument or the code inside the function changes.

# Example 1:

@st.cache_data
def filter_data(df, column, threshold):
    st.write("Filtering data...")  # Runs only when args change
    return df[df[column] > threshold]

# Each time you change threshold or column, cache invalidates and re-runs
filtered = filter_data(df, "sales", threshold=50)


# Example 2:

import streamlit as st
import pandas as pd
import time

@st.cache_data
def load_csv(file_path):
    st.write("🔄 Loading data from file...")  # To see when it runs
    time.sleep(2)  # Simulate slow operation
    return pd.read_csv(file_path)

st.title("🧠 st.cache_data Demo")

# Let user pick one of two CSVs
file_option = st.selectbox(
    "Choose dataset:",
    ("data1.csv", "data2.csv")
)

df = load_csv(file_option)
st.dataframe(df.head())
