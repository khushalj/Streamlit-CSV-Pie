import pandas as pd
import streamlit as st

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('systeminfo.csv')

# Create two new DataFrames with the required columns
host_df = df[['Host Name', 'Registered Owner', 'Registered Organization']]
os_df = df[['OS Name', 'OS Configuration', 'OS Version', 'OS Manufacturer', 'OS Build Type', 'Product ID', 'Original Install Date', 'System Boot Time']]

# Set column headers
host_df.columns = ['Host Name', 'Registered Owner', 'Registered Organization']
os_df.columns = ['OS Name', 'OS Configuration', 'OS Version', 'OS Manufacturer', 'OS Build Type', 'Product ID', 'Original Install Date', 'System Boot Time']

# Show the data in a table
st.write('Host Details')
st.table(host_df)

st.write('OS Properties')
st.table(os_df)
