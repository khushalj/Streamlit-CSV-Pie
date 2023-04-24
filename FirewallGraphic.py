import streamlit as st
import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv("firewall_status.csv")

# Add a new column with tick or cross marks based on the value in the "Enabled" column
df["Status"] = df["Enabled"].apply(lambda x: "✔️" if x else "❌")

# Display the CSV file as a table with tick or cross marks
st.write(df[["Name", "Status"]].style.hide_index())

# Create a comparative bar chart for True and False values in the "Enabled" column
enabled_count = df["Enabled"].value_counts()
fig1 = px.bar(x=enabled_count.index, y=enabled_count.values, title="Firewall Value vs Number of Domains")
fig1.update_xaxes(title_text="Firewall Value")
fig1.update_yaxes(title_text="Number of Domains", tickmode='linear', dtick=1)
st.plotly_chart(fig1)

# Create a pie chart showing the frequency of True and False values in the "Enabled" column
fig2 = px.pie(values=enabled_count.values, names=enabled_count.index, title="Enabled Pie Chart")
st.plotly_chart(fig2)
