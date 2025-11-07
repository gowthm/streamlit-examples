import streamlit as st

st.title("Hello Streamlit")
st.write("This is my first Streamlit app!")

name = st.text_input("Enter your name:")
if st.button("Click"):
    st.success(f"Hello {name}!")