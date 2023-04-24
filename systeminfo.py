import streamlit as st
import pandas as pd

# Load the CSV file
df = pd.read_csv('systeminfo.csv')

# Group the data by Host name, Registered Owner, Registered Organization
host_details = df[['Host Name', 'Registered Owner', 'Registered Organization']] \
    .drop_duplicates() \
    .reset_index(drop=True)

# Group the data by OS Name, OS Configuration, OS Version, OS Manufacturer, OS Build Type, Product ID, Original Install Date, System Boot Time
os_properties = df[['OS Name', 'OS Configuration', 'OS Version', 'OS Manufacturer', 'OS Build Type', 'Product ID', 'Original Install Date', 'System Boot Time']] \
    .drop_duplicates() \
    .reset_index(drop=True)

# Display the Host Details and OS Properties in separate tables
st.write('## Host Details')
st.table(host_details)

st.write('## OS Properties')
st.table(os_properties)
