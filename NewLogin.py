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
            st.write("Click the button to go to the website:")
            # Display button with link to website
            st.button("Go to website", on_click=open_website)
        else:
            st.error("Incorrect username or password")

# Function to open website
def open_website():
    st.experimental_set_query_params(token="abc123")
    st.experimental_redirect("https://khushalj-streamlit-csv-pie-newlogin-32ttdc.streamlit.app/")

# Run the Streamlit app
if __name__ == '__main__':
    app()
