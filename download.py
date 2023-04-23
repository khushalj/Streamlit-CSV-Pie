import streamlit as st
import base64

FILE_PATH = "Report.pdf"

with open(FILE_PATH, "rb") as f:
    contents = f.read()
b64 = base64.b64encode(contents).decode()
href = f"data:file/txt;base64,{b64}"
b64_bytes = base64.b64decode(b64)
st.download_button("Download File", data=b64_bytes, file_name=FILE_PATH, mime="application/pdf")
