import streamlit as st
import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv("output.csv")

# Display the CSV file as a table
st.write(df)

# Create a pie chart showing the frequency of each process
process_count = df["Process"].value_counts()
fig1 = px.pie(values=process_count, names=process_count.index, title="Process Frequency")
st.plotly_chart(fig1)

# Create a bar chart showing the frequency of each local address
address_count = df["LocalAddress"].value_counts()
fig2 = px.bar(x=address_count.index, y=address_count.values, title="Local Address Frequency")
st.plotly_chart(fig2)
