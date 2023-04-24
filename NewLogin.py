import streamlit as st

# Define credentials
CORRECT_USERNAME = "securitybulls"
CORRECT_PASSWORD = "pussyloveraish"

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
            st.success("Logged in!")
            st.experimental_rerun()
            return True
        else:
            st.error("Incorrect username or password")
            return False
    else:
        return False

# Define protected page
def show_protected():
    st.write("# Protected content")
    st.write("You are now logged in!")

# Show appropriate page based on login status
if st.session_state.logged_in:
    show_protected()
else:
    if show_login():
        st.session_state.logged_in = True
        st.redirect("https://khushalj-streamlit-csv-pie-login-hg4xe8.streamlit.app/")
