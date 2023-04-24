import pandas as pd
import streamlit as st

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('systeminfo.csv')

# Create two new DataFrames with the required columns
host_df = df[['Host Name', 'Registered Owner', 'Registered Organization']]
os_df = df[['OS Name', 'OS Configuration', 'OS Version', 'OS Manufacturer', 'OS Build Type', 'Product ID', 'Original Install Date', 'System Boot Time']]

# Set column headers and styles
host_style = "<style>th {color: #f63366; font-size: 20px;}</style>"
os_style = "<style>th {color: #3f88c5; font-size: 20px;}</style>"
st.write(host_style, unsafe_allow_html=True)
st.write(os_style, unsafe_allow_html=True)

# Show the data in a tabular format
st.write('<h2 style="color: #f63366;">Host Details</h2>', unsafe_allow_html=True)
st.table(host_df.style.set_properties(**{'font-size': '20px'}))

st.write('<h2 style="color: #3f88c5;">OS Properties</h2>', unsafe_allow_html=True)
st.table(os_df.style.set_properties(**{'font-size': '20px'}))
