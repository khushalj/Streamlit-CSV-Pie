import streamlit as st
import time

st.title(':green[7 users connected]')

st.subheader('Active:blue[User 1- dave]')
with st.spinner("Loading..."):
    time.sleep(3)
st.divider()
st.subheader('Active:blue[User 2- rahul]')
with st.spinner("Loading..."):
    time.sleep(3)
st.divider()
st.subheader('Active:blue[User 3- gautam]')
with st.spinner("Loading..."):
    time.sleep(3)
st.divider()
st.subheader('Active:blue[User 4- praveen]')
with st.spinner("Loading..."):
    time.sleep(3)
st.divider()
st.subheader('Active:blue[User 5- shrey]')
with st.spinner("Loading..."):
    time.sleep(3)
st.divider()
st.subheader('Inactive:grey[User 6- Khushal]')
with st.spinner("Loading..."):
    time.sleep(3)
st.divider()
st.subheader('Inactive:grey[User 7- Ankan]')
with st.spinner("Loading..."):
    time.sleep(3)
st.divider()
st.subheader('Active:blue[User 8- bharti]')
with st.spinner("Loading..."):
    time.sleep(3)
st.divider()
st.subheader('Active:blue[User 9- vivek]')
