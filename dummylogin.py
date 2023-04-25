import streamlit as st

# Define the correct username and password
USERNAME = 'securitybulls'
PASSWORD = 'khu12'

# Set the title and heading
st.title("Security Bulls Audit Services")
st.header("Welcome Admin")

# Create the login form
login_form = st.form("login_form")
username = login_form.text_input("Username")
password = login_form.text_input("Password", type="password")
submit_button = login_form.form_submit_button("Login")

# Check if the user entered the correct credentials
if submit_button and username == USERNAME and password == PASSWORD:
    st.success("Login successful!")
    # Add your code for what should happen after the user logs in
else:
    st.error("Incorrect username or password")
