import streamlit as st
import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv("your_file.csv")

# Create a comparative bar chart for True and False values in the "Enabled" column
enabled_count = df["Enabled"].value_counts()
fig1 = px.bar(x=enabled_count.index, y=enabled_count.values, title="Enabled Comparative Graph")
st.plotly_chart(fig1)

# Create a pie chart showing the frequency of True and False values in the "Enabled" column
fig2 = px.pie(values=enabled_count.values, names=enabled_count.index, title="Enabled Pie Chart")
st.plotly_chart(fig2)
