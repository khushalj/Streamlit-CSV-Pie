import streamlit as st
import pandas as pd

# Load data from CSV
df = pd.read_csv("systeminfo.csv", header=None, names=["Name", "Value"])

# Define groups of properties
host_details = ["Host Name", "Registered Owner", "Registered Organization"]
os_properties = ["OS Name", "OS Configuration", "OS Version", "OS Manufacturer", "OS Build Type", "Product ID", "Original Install Date", "System Boot Time"]
hardware_properties = ["System Manufacturer", "System Model", "System Type", "Processor(s)", "[01]", "Boot Device"]
logical_properties = ["Windows Directory", "System Directory", "BIOS Version"]
locale_properties = ["System Locale", "Input Locale", "Time Zone"]
memory_properties = ["Total Physical Memory", "Available Physical Memory", "Virtual Memory", "Virtual Memory", "Virtual Memory"]
network_properties = ["Domain", "Logon Server", "Hotfix(s)", "[01]", "[02]", "[03]", "[04]", "Network Card(s)", "[01]", "Connection Name", "DHCP Enabled", "DHCP Server", "IP address(es)", "[01]", "[02]", "Connection Name", "Status", "[03]", "Connection Name", "DHCP Enabled", "DHCP Server", "IP address(es)", "[01]", "[02]", "[04]", "Connection Name", "DHCP Enabled", "DHCP Server", "IP address(es)", "[01]", "[02]", "[05]", "Connection Name", "DHCP Enabled", "IP address(es)", "[01]", "[02]", "[06]", "Connection Name", "Status", "[07]", "Connection Name", "DHCP Enabled", "IP address(es)"]

# Create separate dataframes for each group
host_details_df = df[df["Name"].isin(host_details)]
os_properties_df = df[df["Name"].isin(os_properties)]
hardware_properties_df = df[df["Name"].isin(hardware_properties)]
logical_properties_df = df[df["Name"].isin(logical_properties)]
locale_properties_df = df[df["Name"].isin(locale_properties)]
memory_properties_df = df[df["Name"].isin(memory_properties)]
network_properties_df = df[df["Name"].isin(network_properties)]

# Set page title
st.set_page_config(page_title="System Info")

# Display host details table
st.write("## Host Details")
st.dataframe(host_details_df.style.set_properties(**{"width": "100px"}), height=300)

# Display OS properties table
st.write("## OS Properties")
st.dataframe(os_properties_df.style.set_properties(**{"width": "100px"}), height=400)

# Display hardware properties table
st.write("## Hardware Properties")
st.dataframe(hardware_properties_df.style.set_properties(**{"width": "100px"}), height=400)

# Display logical properties table
st.write("## Logical Properties")
st.dataframe(logical_properties_df.style.set_properties(**{"width": "100px"}), height=200)

# Display locale properties table
st.write("## Locale Properties")
st.dataframe(locale_properties_df.style.set_properties(**{"width": "100px"}), height=200)

# Display memory properties table
st.write("## Memory Properties")
st.dataframe(memory_properties_df.style.set_properties(**{"width": "100px"}), height=200)

# Display network properties table
st.write("## Network & Network Adapter Properties")
st.dataframe(network_properties_df.style.set_properties(**{"width": "100px"}), height=600)
