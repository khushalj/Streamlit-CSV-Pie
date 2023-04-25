import streamlit as st
import pandas as pd

# read csv file
df = pd.read_csv('systeminfo.csv', names=['Name', 'Value'])

# create sections
sections = {
    'Host Details': ['Host Name', 'Registered Owner', 'Registered Organization'],
    'OS Properties': ['OS Name', 'OS Configuration', 'OS Version', 'OS Manufacturer', 'OS Build Type', 'Product ID', 'Original Install Date', 'System Boot Time'],
    'Hardware Properties': ['System Manufacturer', 'System Model', 'System Type', 'Processor(s)', '[01]', 'Boot Device'],
    'Logical Properties': ['Windows Directory', 'System Directory', 'BIOS Version'],
    'Locale Properties': ['System Locale', 'Input Locale', 'Time Zone'],
    'Memory Properties': ['Total Physical Memory', 'Available Physical Memory', 'Virtual Memory', 'Virtual Memory', 'Virtual Memory'],
    'Network & Network Adapter Properties': ['Domain', 'Logon Server', 'Hotfix(s)', '[01]', '[02]', '[03]', '[04]', 'Network Card(s)', '[01]', 'Connection Name', 'DHCP Enabled', 'DHCP Server', 'IP address(es)', '[01]', '[02]', 'Connection Name', 'Status', '[03]', 'Connection Name', 'DHCP Enabled', 'DHCP Server', 'IP address(es)', '[01]', '[02]', '[04]', 'Connection Name', 'DHCP Enabled', 'DHCP Server', 'IP address(es)', '[01]', '[02]', '[05]', 'Connection Name', 'DHCP Enabled', 'IP address(es)', '[01]', '[02]', '[06]', 'Connection Name', 'Status', '[07]', 'Connection Name', 'DHCP Enabled', 'IP address(es)'],
    'hypervisor': ['Hyper-V Requirements'],
    'Hotfix Details': ['Hotfix(s)', '[01]', '[02]', '[03]', '[04]']
}

# create dictionary to store values for each section
section_values = {}
for section in sections:
    section_values[section] = {}

# loop through rows of dataframe and populate section values dictionary
for index, row in df.iterrows():
    for section, section_names in sections.items():
        if row['Name'] in section_names:
            section_values[section][row['Name']] = row['Value']

# display sections
st.set_page_config(page_title="System Information")
for section, section_names in sections.items():
    st.header(section)
    section_df = pd.DataFrame(section_values[section].items(), columns=['Name', 'Value'])
    section_df = section_df.loc[section_df['Name'].isin(section_names)]
    section_df['Value'] = section_df['Value'].apply(lambda x: '✔️' if x == 'True' else ('❌' if x == 'False' else x)) # add tick or cross for True/False values
    st.dataframe(section_df.style.set_properties(**{'width': '100px'}), width=800)
