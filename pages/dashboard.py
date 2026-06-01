import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("📊 Sustainability Dashboard")

conn = sqlite3.connect("data/waste_data.db")
df = pd.read_sql_query("SELECT * FROM waste_records", conn)

st.metric("Total Items Processed", len(df))
st.metric("Total CO₂ Saved (kg)", round(df["co2_saved"].sum(), 2))

fig = px.pie(df, names="label", title="Waste Distribution")
st.plotly_chart(fig)

fig2 = px.line(df, x="timestamp", y="co2_saved", title="CO₂ Savings Over Time")
st.plotly_chart(fig2)
