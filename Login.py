import pickle
from pathlib import Path
import streamlit as st
import yaml
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import altair as alt
from time import strftime
import time

# Define the correct username and password
USERNAME = 'Khushal'
PASSWORD = '7eae7644'

# --- USER AUTHENTICATION ---
def login():
    return st.text_input('Username'), st.text_input('Password', type='password')

def authenticate(username, password):
    return username == USERNAME and password == PASSWORD

def logout():
    session_state = st.session_state
    session_state['authenticated'] = False

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    st.warning("Please enter your username and password")
    username, password = login()
    if authenticate(username, password):
        st.session_state['authenticated'] = True
    else:
        st.error("Username/password is incorrect")
else:
    # ---- SIDEBAR ----
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    with st.sidebar:
        selected = option_menu(
            menu_title= "Dashboard",
            options=["Home", "Network Audit", "OS Audit", "Vulnerability Assessment", "Malware Logs"],
            icons=["house", "ethernet","motherboard","braces asterisk","envelope"],
            menu_icon="cast",
            default_index=0,
        )
    if selected== "Home":
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
            options=["Firewall Stats", "Open-Ports Logs", "Network Stats"],
            icons=["bricks", "displayport", "fire"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )
        # st.title(f"{selected}")
        if select == "Open-Ports Logs":
            st.title(f"{select}")
            port()
        if select == "Firewall Stats":
            st.title(f"{select}")
            firewall()
        if select == "Network Stats":
            st.title(f"{select}")
            netstats()



    if selected == "OS Audit":
        select = option_menu(
            menu_title="OS Audit",
            options=["OS Details", "System Version", "Peripheral Devices"],
            icons=["bricks", "displayport", "fire"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )
        if select == "OS Details":
            st.title(f"{select}")
        if select == "System Version":
            st.title(f"{select}")
        if select == "Peripheral Devices":
            st.title(f"{select}")

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


