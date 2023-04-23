import pickle
from pathlib import Path
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth
import yaml
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
# --- USER AUTHENTICATION ---
with open('/Users/aishworyann/Desktop/Streamlit Authenticator/config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')
def port():
    st.title("Port Status")
    # Upload CSV
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        # Create a dictionary to map boolean values to checkmark or cross symbols
        # status_dict = {True: "✅", False: "❌"}
        # # Replace the boolean values with checkmark or cross symbols
        # df["Enabled"] = df["Enabled"].map(status_dict)
        #Table BG
        st.markdown(
            '<style>div.row-widget.stRadio > div{background-color: #f4f4f4}</style>',
            unsafe_allow_html=True,
        )
        total_ports = len(df)
        open_ports = len(df[df['State'] == 'Open'])
        close_ports = total_ports - open_ports
        open_percentage = round(open_ports / total_ports * 100, 2)
        close_percentage = round(close_ports / total_ports * 100, 2)

        # Create a pie chart to display the data
        data = {'State': ['Open', 'Close'], 'Percentage': [open_percentage, close_percentage]}
        fig = px.pie(data, values='Percentage', names='State')
        left_column, right_column = st.columns(2)
        # Display the pie chart
        with left_column:
            st.write(df)
        with right_column:
            st.plotly_chart(fig)

        # Display table



if authentication_status == False:
    st.error("Username/password is incorrect")
if authentication_status == None:
    st.warning("Please enter your username and password")
if authentication_status:
    # ---- SIDEBAR ----
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    with st.sidebar:
        selected = option_menu(
            menu_title= "Dashboard",
            options=["Home", "Netowrk Audit", "OS Audit", "Vulnerability Assessment", "Malware Logs"],
            icons=["house", "ethernet","motherboard","braces asterisk","envelope"],
            menu_icon="cast",
            default_index=0,
        )
    if selected== "Home":
        st.title(f"{selected}")
    if selected == "Netowrk Audit":
        st.title(f"{selected}")
    with st.sidebar:
        selected = option_menu(
            menu_title="Dashboard",
            options=["Firewall","Open Port Logs"],
            icons=["house", "activity", "envelope","","",""],
            menu_icon="cast",
            default_index=0,
        )
    if selected == "OS Audit":
        st.title(f"{selected}")
    if selected == "Vulnerability Assessment":
        st.title(f"{selected}")
    if selected == "Malware Logs":
        st.title(f"{selected}")

