import pickle
from pathlib import Path
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth
import yaml
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import altair as alt
from time import strftime
import time
# --- USER AUTHENTICATION ---
# with open('config.yaml') as file:
#     config = yaml.load(file, Loader=yaml.SafeLoader)
# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# name, authentication_status, username = authenticator.login('Login', 'main')

def firewall():
    # Upload CSV
    # uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    df = pd.read_csv("firewall_status.csv")
    # Add a new column with tick or cross marks based on the value in the "Enabled" column
    df["Status"] = df["Enabled"].apply(lambda x: "✅" if x else "❌")
    # color of tick and cross marks based on the value in the "Enabled" column
    df["Status"] = df["Enabled"].apply(lambda x: "✅" if x else "❌")

    col1, col2 = st.columns(2)
    enabled_count = df["Enabled"].value_counts()
    colors = ["green", "red"]
    with col1:
        # Display the CSV file as a table with tick or cross
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        st.table(df[["Name", "Status"]].style.hide_index())

    with col2:
# Create a pie chart showing the frequency of True and False values in the "Enabled" column
        fig2 = px.pie(values=enabled_count.values, names=enabled_count.index, title="Status of Firewall Across Domains",
              color=enabled_count.index, color_discrete_sequence=colors)
        st.plotly_chart(fig2)

 # comparative bar chart for True and False values in the "Enabled" column

    fig1 = px.bar(x=enabled_count.index, y=enabled_count.values,
                      title="Comparative analysis of Active & Inactive Firewall on Domains", color=enabled_count.index,
                      color_discrete_sequence=colors)
    fig1.update_xaxes(title_text="Firewall Value")
    fig1.update_yaxes(title_text="Number of Domains", tickmode='linear', dtick=1)
    st.plotly_chart(fig1)

def os_version():
    csv_file_path = "osversion8.csv"
    dataframe = pd.read_csv(csv_file_path)
    # st.header("OS Version and Properties")
    st.image("image.png")
    st.table(dataframe)
    

def netstats():
    # file = st.file_uploader("Upload CSV file", type=["csv"])
    file = "network-stats.csv"
    if file:
        df = pd.read_csv(file)

        # Create a bar chart of InterfaceAlias and Source
        chart = alt.Chart(df).mark_bar().encode(
            x='InterfaceAlias',
            y='count()',
            color='Source'
        ).properties(
            width=600,
            height=400
        )
        st.altair_chart(chart)

        # Create a table of statistics for each InterfaceAlias
        interfaces = df['InterfaceAlias'].unique()
        for interface in interfaces:
            st.write('## ' + interface)
            subset = df[df['InterfaceAlias'] == interface]
            subset = subset.drop(columns=['ifAlias', 'ifDesc', 'Caption', 'Description', 'ElementName', 'InstanceID',
                                          'InterfaceDescription', 'Name', 'Source', 'SystemName'])
            st.write(subset)

def peripheral():
    #st.title("Peripherals Status")

    filename = "PeripheralsAndAdaptersReport.csv"
    df = pd.read_csv(filename)
    status_dict = {"OK": "✅", "ERROR": "❌"}
    df["Status"] = df["Status"].map(status_dict)

    st.markdown(
        '<style>div.row-widget.stRadio > div{background-color: #f4f4f4}</style>',
        unsafe_allow_html=True,
    )
    st.write(df)

    total_class = len(df)
    system_adap = len(df[df['Class'] == 'System'])
    net_adap = total_class - system_adap
    System_percentage = round(system_adap/ total_class * 100, 2)
    Net_percentage = round( net_adap / total_class* 100, 2)

    data = {'Class': ['System', 'Net'], 'Percentage': [System_percentage, Net_percentage]}
    fig1 = px.pie(data, values='Percentage', names='Class', color_discrete_sequence=['yellow', 'teal'])

    st.plotly_chart(fig1)

def portList():
    df = pd.read_csv("output.csv")
    # st.set_page_config(page_title="Listening Port Stats")
    # Bold Bold headings dekhlo
    # st.markdown("<h1 style='text-align: center; font-weight: bold;'>Listening Port Stats 👂🏻</h1>",
    #             unsafe_allow_html=True)
    # Gol Gol Pie Dekho
    process_count = df["Process"].value_counts()
    fig1 = px.pie(values=process_count, names=process_count.index, title="Process Frequency")
    st.plotly_chart(fig1)

    # Bar Chart 🌚
    address_count = df["LocalAddress"].value_counts()
    fig2 = px.bar(x=address_count.index, y=address_count.values, title="Local Address Frequency")
    st.plotly_chart(fig2)

    # Table m sab dekhlo
    st.write(df.style.set_properties(**{'font-weight': 'bold'}))


st.sidebar.title(f"Welcome Gend Bhai !")

with st.sidebar:
        selected = option_menu(
            menu_title= "Dashboard",
            options=["Home", "Notification","Network Audit", "OS Audit", "Vulnerability Assessment", "Malware Logs"],
            icons=["house", "ethernet","motherboard","braces asterisk","envelope"],
            menu_icon="cast",
            default_index=0,
        )
if selected=="Home":
    st.title(f"{selected}")

if selected== "Notification":
        st.title(f"{selected}")
        st.subheader('Notifications 🗒')
        with st.spinner("Listening..."):
            time.sleep(3)
        st.error(' Firewall are not enabled for one or more Domains')
        with st.spinner("Listening..."):
            time.sleep(2)
        st.error(' Ports [21] & [22] are open')
        with st.spinner("Listening..."):
            time.sleep(1)
        st.error(' No active backup present')
        with st.spinner("Listening..."):
            time.sleep(2)
        st.success(' System is Up-to Date')
        with st.spinner("Listening..."):
            time.sleep(3)
        st.success(' 2 Active Users Found')

if selected == "Network Audit":
        select = option_menu(
            menu_title="Network Audit",
            options=["Listening Ports", "Network Stats","Firewall Stats"],
            icons=["bricks", "displayport", "fire"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )
        # st.title(f"{selected}")
        if select == "Listening Ports":
            st.title(f"{select}")
            portList()
        if select == "Firewall Stats":
            st.title(f"{select}")
            firewall()
        if select == "Network Stats":
            st.title(f"{select}")
            netstats()



if selected == "OS Audit":
        select = option_menu(
            menu_title="OS Audit",
            options=["OS Details and System Version", "Peripheral Devices"],
            icons=["bricks", "displayport", "fire"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )
        if select == "OS Details and System Version":
            st.title(f"{select}")
            os_version()
        if select == "Peripheral Devices":
            st.title(f"{select}")
            peripheral()


if selected == "Vulnerability Assessment":
        select = option_menu(
            menu_title="Vulnerability Assessment",
            options=["Assessment 1", "Assessment 2", "Assessment 3"],
            icons=["file-bar-graph", "file-bar-graph", "file-bar-graph"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )
        if select == "Assessment 1":
            st.title(f"{select}")
        if select == "Assessment 2":
            st.title(f"{select}")
        if select == "Assessment 3":
            st.title(f"{select}")

if selected == "Malware Logs":
        st.title(f"{selected}")


