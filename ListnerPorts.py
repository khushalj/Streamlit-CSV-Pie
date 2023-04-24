import streamlit as st
import pandas as pd
import plotly.express as px

# CSV Padhle bhai
df = pd.read_csv("output.csv")

st.set_page_config(page_title="Listening Port Stats")

# Bold Bold headings dekhlo
st.markdown("<h1 style='text-align: center; font-weight: bold;'>LocalAddress Listening Port Stats</h1>", unsafe_allow_html=True)

# Gol Gol Pie Dekho
process_count = df["Process"].value_counts()
fig1 = px.pie(values=process_count, names=process_count.index, title="Process Frequency")
st.plotly_chart(fig1)

# Bar Chart 🌚
address_count = df["LocalAddress"].value_counts()
fig2 = px.bar(x=address_count.index, y=address_count.values, title="Local Address Frequency")
st.plotly_chart(fig2)

# Table m sab dekhlo
st.write(df.style.set_properties(**{'font-weight': 'bold'}))
