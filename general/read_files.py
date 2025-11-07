import streamlit as st
import pandas as pd

st.title("CSV Data Analyzar")

file = st.file_uploader("Upload CSV", type=["csv"])

if file is not None:

    df = pd.read_csv(file)
    st.subheader("Data preview")

    st.dataframe(df.head()) # Show first 5 rows

    st.subheader("Data Summary")

    st.write("Number of rows:", df.shape[0])
    st.write("Number of columns:", df.shape)

    # Column selection

    numeric_cols = df.select_dtypes(include=['number', 'datetime']).columns.tolist()

    if numeric_cols:
        st.subheader("Quick Visualization")
        selected_col = st.selectbox("Choose a numeric column to visualize", numeric_cols)
        st.bar_chart(df[selected_col])
    else:
        st.info("No numberic columns available for chart.")







    #st.bar_chart(df.select_dtypes('number'))
