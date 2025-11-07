# long-lived or expensive resources.
'''
st.cache_resource is used when you want to create something once (like a database connection or model)
and reuse the same instance across reruns — instead of recreating it each time.

Unlike st.cache_data, it does not reload when inputs change — because resources aren’t recomputed, they’re reused.
'''

import streamlit as st
import pandas as pd
import sqlite3

@st.cache_resource
def get_connection():
    return sqlite3.connect("users.db")

@st.cache_data
def get_data(conn):
    return pd.read_sql("SELECT * FROM users", conn)

st.title("📦 Combined Cache Example")

conn = get_connection()
df = get_data(conn)
st.dataframe(df.head())
