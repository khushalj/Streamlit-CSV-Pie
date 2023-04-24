import streamlit as st
import pandas as pd

# Read in the CSV file
df = pd.read_csv("systeminfo.csv")

# Group the columns and rename the headers
host_details = df[["Host Name", "Registered Owner", "Registered Organization"]]
host_details.columns = ["Host Name", "Owner", "Organization"]

os_properties = df[["OS Name", "OS Configuration", "OS Version", "OS Manufacturer", "OS Build Type", "Product ID", "Original Install Date", "System Boot Time"]]
os_properties.columns = ["OS Name", "OS Configuration", "OS Version", "OS Manufacturer", "OS Build Type", "Product ID", "Install Date", "Boot Time"]

# Display the data in tabular form
st.write("## Host Details")
st.table(host_details)

st.write("## OS Properties")
st.table(os_properties)
