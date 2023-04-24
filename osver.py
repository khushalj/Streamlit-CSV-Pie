import streamlit as st
import pandas as pd
csv_file_path = "osversion8.csv"
dataframe = pd.read_csv(csv_file_path)
st.header("OS Version and Properties")
st.table(dataframe)
