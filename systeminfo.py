import pandas as pd
import streamlit as st

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('systeminfo.csv')

# Create two new DataFrames with the required columns
host_df = df[['Host Name', 'Registered Owner', 'Registered Organization']]
os_df = df[['OS Name', 'OS Configuration', 'OS Version', 'OS Manufacturer', 'OS Build Type', 'Product ID', 'Original Install Date', 'System Boot Time']]

# Set column headers and styles
host_style = "<style>h2 {color: #f63366;}</style>"
os_style = "<style>h2 {color: #3f88c5;}</style>"
st.write(host_style, unsafe_allow_html=True)
st.write(os_style, unsafe_allow_html=True)

# Show the data in a tabular format
col1, col2 = st.beta_columns(2)

with col1:
    st.write('<h2>Host Details</h2>', unsafe_allow_html=True)
    st.table(host_df.style.set_properties(**{'font-size': '20px'}))

with col2:
    st.write('<h2>OS Properties</h2>', unsafe_allow_html=True)
    st.table(os_df.style.set_properties(**{'font-size': '20px'})))
