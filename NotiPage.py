from tkinter import *
import random
import webbrowser
from tkinter import ttk
from time import strftime
from PIL import Image, ImageTk
import streamlit as st
import time
st.set_page_config(
    page_title="Dashboard",
    page_icon="🕵",
)
st.title("Audit Dashboard",)
st.subheader('Notifications 🗒')
with st.spinner("Listening..."):
    time.sleep(3)
st.error(' Firewall are not enabled for one or more Domains', icon="⚠")
with st.spinner("Listening..."):
    time.sleep(2)
st.error(' Ports [21] & [22] are open', icon="⚠")
with st.spinner("Listening..."):
    time.sleep(1)
st.error(' No active backup present', icon="⚠")
with st.spinner("Listening..."):
    time.sleep(2)
st.success(' System is Up-to Date', icon = "🟢")
with st.spinner("Listening..."):
    time.sleep(3)
st.success(' 2 Active Users Found', icon = "🟢")

# Define a function that checks a condition and generates a notification if true
def check_condition():
    if some_condition:
        st.experimental_notify("Notification", "The condition is true")



#Download
import streamlit as st
import pandas as pd

# Load some example data
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

# Define a function to download a CSV file
def download_csv(data):
    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode() 
    href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV file</a>'
    return href

# Render a download button
if st.button('Download data as CSV file'):
    st.markdown(download_csv(data), unsafe_allow_html=True)



# Add a sleep timer to simulate some background process
time.sleep(5)
