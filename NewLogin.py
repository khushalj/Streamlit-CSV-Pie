import streamlit as st

# Define credentials
CORRECT_USERNAME = "user"
CORRECT_PASSWORD = "password"

# Define login page
def show_login():
    # Show login form
    st.write("# Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login = st.button("Log in")

    # Check credentials
    if login:
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Incorrect username or password")

# Define protected page
def show_protected():
    st.write("# Protected content")
    st.write("You are now logged in!")

# Show appropriate page based on login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    show_protected()
else:
    show_login()
