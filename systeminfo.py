import streamlit as st
import pandas as pd

# read csv file
data = pd.read_csv("system_info.csv", names=["Name", "Value"])

# create dictionary to group properties
groups = {
    "Host Details": ["Host Name", "Registered Owner", "Registered Organization"],
    "OS Properties": ["OS Name", "OS Configuration", "OS Version", "OS Manufacturer", "OS Build Type", "Product ID", "Original Install Date", "System Boot Time"],
    "Hardware Properties": ["System Manufacturer", "System Model", "System Type", "Processor(s)", "[01]", "Boot Device"],
    "Logical Properties": ["Windows Directory", "System Directory", "BIOS Version"],
    "Locale Properties": ["System Locale", "Input Locale", "Time Zone"],
    "Memory Properties": ["Total Physical Memory", "Available Physical Memory", "Virtual Memory", "Virtual Memory", "Virtual Memory"],
    "Network & Network Adapter Properties": ["Domain", "Logon Server", "Hotfix(s)", "[01]", "[02]", "[03]", "[04]", "Network Card(s)", "[01]", "Connection Name", "DHCP Enabled", "DHCP Server", "IP address(es)", "[01]", "[02]", "Connection Name", "Status", "[03]", "Connection Name", "DHCP Enabled", "DHCP Server", "IP address(es)", "[01]", "[02]", "[04]", "Connection Name", "DHCP Enabled", "DHCP Server", "IP address(es)", "[01]", "[02]", "[05]", "Connection Name", "DHCP Enabled", "IP address(es)", "[01]", "[02]", "[06]", "Connection Name", "Status", "[07]", "Connection Name", "DHCP Enabled", "IP address(es)"],
    "Hypervisor": ["Hyper-V Requirements"],
    "Hotfix(s) Details": ["Hotfix(s)"]
}

# create empty dataframes for each group
dfs = {group: pd.DataFrame(columns=["Name", "Value"]) for group in groups}

# fill dataframes with corresponding properties
for index, row in data.iterrows():
    for group, properties in groups.items():
        if row["Name"] in properties:
            dfs[group] = dfs[group].append(row, ignore_index=True)
            break

# set page title
st.set_page_config(page_title="System Info")

# display each group as a table
for group, df in dfs.items():
    st.write(f"## {group}")
    st.dataframe(df.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])]), width=800)

