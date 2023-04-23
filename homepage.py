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
with st.spinner("Computing..."):
    time.sleep(3)
st.error('firewall parameters are not enabled', icon="⚠")
with st.spinner("Computing..."):
    time.sleep(3)
st.error('2 major service ports open', icon="⚠")
with st.spinner("Computing..."):
    time.sleep(3)
st.error('Active backup not present', icon="⚠")
with st.spinner("Computing..."):
    time.sleep(3)
st.success('windows updated', icon = "🟢")
with st.spinner("Computing..."):
    time.sleep(3)
st.success('7 active users found', icon = "🟢")
st.balloons()


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
