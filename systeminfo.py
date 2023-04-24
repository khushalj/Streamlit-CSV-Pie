import streamlit as st
import pandas as pd

# Load the CSV file
df = pd.read_csv("systeminfo.csv")

# Group the details of the Host name, Registered Owner, and Registered Organization together
host_details = df.loc[df['Name'].isin(['Host Name', 'Registered Owner', 'Registered Organization'])]

# Group the details of the OS Name, OS Configuration, OS Version, OS Manufacturer, OS Build Type, Product ID, Original Install Date, and System Boot Time together
os_properties = df.loc[df['Name'].isin(['OS Name', 'OS Configuration', 'OS Version', 'OS Manufacturer', 'OS Build Type', 'Product ID', 'Original Install Date', 'System Boot Time'])]

# Group the details of the System Manufacturer, System Model, System Type, Processor(s), [01], Boot Device together
hardware_properties = df.loc[df['Name'].isin(['System Manufacturer', 'System Model', 'System Type', 'Processor(s)', '[01]', 'Boot Device'])]

# Group the details of the Windows Directory, System Directory, and BIOS Version together
logical_properties = df.loc[df['Name'].isin(['Windows Directory', 'System Directory', 'BIOS Version'])]

# Group the details of the System Locale, Input Locale, and Time Zone together
locale_properties = df.loc[df['Name'].isin(['System Locale', 'Input Locale', 'Time Zone'])]

# Group the details of the Total Physical Memory, Available Physical Memory, and Virtual Memory together
memory_properties = df.loc[df['Name'].isin(['Total Physical Memory', 'Available Physical Memory', 'Virtual Memory', 'Virtual Memory', 'Virtual Memory'])]

# Set the page title and width
st.set_page_config(page_title="System Information", layout="wide")

# Display the tables with headings and same width
st.write("Host Details")
st.dataframe(host_details, width=600, height=300)

st.write("OS Properties")
st.dataframe(os_properties, width=600, height=300)

st.write("Hardware Properties")
st.dataframe(hardware_properties, width=600, height=300)

st.write("Logical Properties")
st.dataframe(logical_properties, width=600, height=300)

st.write("Locale Properties")
st.dataframe(locale_properties, width=600, height=300)

st.write("Memory Properties")
st.dataframe(memory_properties, width=600, height=300)
