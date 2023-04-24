import streamlit as st

# Define username and password
username = "abc"
password = "abc"

# Define Streamlit app
def app():
    # Set page title
    st.set_page_config(page_title="Login Page")

    # Create login form
    st.subheader("Login")
    user_input = st.text_input("Enter username")
    pass_input = st.text_input("Enter password", type="password")

    # Check if login details are correct
    if st.button("Submit"):
        if user_input == username and pass_input == password:
            st.success("Login successful!")
            st.write("Redirecting to website...")
            # Redirect to website
            st.session_state.is_authenticated = True
            js = "window.open('https://khushalj-streamlit-csv-pie-login-hg4xe8.streamlit.app/','_blank')"
            html = '<img src onerror="{}">'.format(js)
            div = '<div style="display:none">{}</div>'.format(html)
            st.markdown(div, unsafe_allow_html=True)
        else:
            st.error("Incorrect username or password")

# Run the Streamlit app
if __name__ == '__main__':
    app()
