import streamlit as st

# Define credentials
CORRECT_USERNAME = "user"
CORRECT_PASSWORD = "password"

# Define login page
def show_login(redirect_url):
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
            st.experimental_set_query_params(logged_in=True)
            st.experimental_set_query_params(redirect_url='https://khushalj-streamlit-csv-pie-login-hg4xe8.streamlit.app/')
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
    # Check if redirect URL is set
    if "redirect_url" in st.experimental_get_query_params():
        redirect_url = st.experimental_get_query_params()["redirect_url"][0]
        st.experimental_set_query_params()
        st.experimental_rerun()
        st.write(f"Redirecting to {redirect_url}...")
        # Add a small delay to allow the redirect message to display
        st.experimental_sleep(1)
        st.experimental_set_query_params()
        st.experimental_rerun()
        st.redirect(redirect_url)
    else:
        show_protected()
else:
    show_login("https://www.google.com")
