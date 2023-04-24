import streamlit as st
import pandas as pd

# Load the CSV file
df = pd.read_csv("systeminfo.csv")

# Group the details of the Host name, Registered Owner, and Registered Organization together
host_details = df.loc[df['Name'].isin(['Host Name', 'Registered Owner', 'Registered Organization'])]

# Group the details of the OS Name, OS Configuration, OS Version, OS Manufacturer, OS Build Type, Product ID, Original Install Date, and System Boot Time together
os_properties = df.loc[df['Name'].isin(['OS Name', 'OS Configuration', 'OS Version', 'OS Manufacturer', 'OS Build Type', 'Product ID', 'Original Install Date', 'System Boot Time'])]

# Set the page title
st.set_page_config(page_title="System Information")

# Display the tables with headings and set the width to 100%
st.write("Host Details")
st.dataframe(host_details.style.set_table_styles([{'selector': 'table', 'props': [('width', '100%')]}]), width=800, height=300)

st.write("OS Properties")
st.dataframe(os_properties.style.set_table_styles([{'selector': 'table', 'props': [('width', '100%')]}]), width=800, height=300)
