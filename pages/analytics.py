import streamlit as st
import sqlite3
import pandas as pd

st.title("📈 Advanced Analytics")

conn = sqlite3.connect("data/waste_data.db")
df = pd.read_sql_query("SELECT * FROM waste_records", conn)

st.bar_chart(df.groupby("label").size())
