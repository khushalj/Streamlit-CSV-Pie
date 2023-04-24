import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Firewall Analysis")

# Read the CSV file
df = pd.read_csv("firewall_status.csv")

# Add a new column with tick or cross marks based on the value in the "Enabled" column
df["Status"] = df["Enabled"].apply(lambda x: "✅" if x else "❌")

# color of tick and cross marks based on the value in the "Enabled" column
df["Status"] = df["Enabled"].apply(lambda x: "✅" if x else "❌")

# comparative bar chart for True and False values in the "Enabled" column
enabled_count = df["Enabled"].value_counts()
colors = ["green", "red"]
fig1 = px.bar(x=enabled_count.index, y=enabled_count.values, title="Comparative analysis of Active & Inactive Firewall on Domains", color=enabled_count.index, color_discrete_sequence=colors)
fig1.update_xaxes(title_text="Firewall Value")
fig1.update_yaxes(title_text="Number of Domains", tickmode='linear', dtick=1)
st.plotly_chart(fig1)

# Create a pie chart showing the frequency of True and False values in the "Enabled" column
fig2 = px.pie(values=enabled_count.values, names=enabled_count.index, title="Status of Firewall Across Domains", color=enabled_count.index, color_discrete_sequence=colors)
st.plotly_chart(fig2)

# Display the CSV file as a table with tick or cross 
st.write(df[["Name", "Status"]].style.hide_index())
