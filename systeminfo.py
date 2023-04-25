import streamlit as st
import pandas as pd

# Read the CSV file
df = pd.read_csv('system_info.csv', header=None, names=['Name', 'Value'])

# Define the groups
host_group = ['Host Name', 'Registered Owner', 'Registered Organization']
os_group = ['OS Name', 'OS Configuration', 'OS Version', 'OS Manufacturer', 'OS Build Type', 'Product ID', 'Original Install Date', 'System Boot Time']
hardware_group = ['System Manufacturer', 'System Model', 'System Type', 'Processor(s)', '[01]', 'Boot Device']
logical_group = ['Windows Directory', 'System Directory', 'BIOS Version']
locale_group = ['System Locale', 'Input Locale', 'Time Zone']
memory_group = ['Total Physical Memory', 'Available Physical Memory', 'Virtual Memory', 'Virtual Memory', 'Virtual Memory']
network_group = ['Domain', 'Logon Server', 'Connection Name', 'DHCP Enabled', 'DHCP Server', 'IP address(es)', '[01]', '[02]', '[03]', '[04]', 'Network Card(s)', '[01]', '[02]', 'Connection Name', 'Status', '[03]', 'Connection Name', 'DHCP Enabled', 'DHCP Server', 'IP address(es)', '[01]', '[02]', '[04]', 'Connection Name', 'DHCP Enabled', 'DHCP Server', 'IP address(es)', '[01]', '[02]', '[05]', 'Connection Name', 'DHCP Enabled', 'IP address(es)', '[01]', '[02]', '[06]', 'Connection Name', 'Status', '[07]', 'Connection Name', 'DHCP Enabled', 'IP address(es)', '[01]', '[02]']
hypervisor_group = ['Hyper-V Requirements']

# Group the data by the defined groups
grouped_df = df.groupby(pd.Series([col in host_group for col in df['Name']]).cumsum())
grouped_df = list(grouped_df)[1:]
grouped_data = []
for group in grouped_df:
    group_name = group[1]['Name'].iloc[0]
    group_df = group[1].set_index('Name')['Value']
    if group_name == 'Processor(s)':
        group_df = group_df.str.split('\n').explode().str.replace(r'^\s+', '', regex=True).reset_index(name='Value').set_index('Name')['Value']
    elif group_name in ['IP address(es)', '[01]', '[02]', '[03]', '[04]', '[05]', '[06]', '[07]']:
        group_df = group_df.str.split('\n').explode().reset_index(name='Value').set_index('Name')['Value']
    grouped_data.append((group_name, group_df))

# Define the hotfix details group
hotfix_df = df[df['Name'] == 'Hotfix(s)'].reset_index(drop=True)
if not hotfix_df.empty:
    hotfix_details = []
    for i in range(1, len(hotfix_df.columns)):
        hotfix_details.append((hotfix_df.columns[i], hotfix_df.iloc[0][i]))
    grouped_data.append(('Hotfix Details', pd.Series(hotfix_details)))

# Display the groups
for group in grouped_data:
    st.write(f"## {group[0]}")
    st.write(group[1])
