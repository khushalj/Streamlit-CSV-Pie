import streamlit as st
import pandas as pd

# Read the CSV file
df = pd.read_csv("system_info.csv")

# Select columns for Host Details and OS Properties
host_cols = ["Host Name", "Registered Owner", "Registered Organization"]
os_cols = ["OS Name", "OS Configuration", "OS Version", "OS Manufacturer", "OS Build Type", "Product ID", "Original Install Date", "System Boot Time"]

# Create dataframes for Host Details and OS Properties
host_df = df[host_cols].transpose()
os_df = df[os_cols].transpose()

# Set column and row names
host_df.columns = [""]
os_df.columns = [""]

# Create style strings for headers
host_style = "<style>h3 {color: #f63366;}</style>"
os_style = "<style>h3 {color: #3f88c5;}</style>"

# Write headers and data for Host Details
st.markdown(host_style, unsafe_allow_html=True)
st.write("<h3>Host Details</h3>", unsafe_allow_html=True)
for column in host_df.columns:
    st.write(f"<h3>{column}</h3>", host_df[column].iloc[0], unsafe_allow_html=True)

# Write headers and data for OS Properties
st.markdown(os_style, unsafe_allow_html=True)
st.write("<h3>OS Properties</h3>", unsafe_allow_html=True)
for column in os_df.columns:
    st.write(f"<h3>{column}</h3>", os_df[column].iloc[0], unsafe_allow_html=True)
