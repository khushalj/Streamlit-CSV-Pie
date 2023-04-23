import streamlit as st
import pandas as pd

# Define login function to authenticate user
def login():
    st.sidebar.header("Login")

    # Define credentials
    LOGIN_ID = "securitybulls"
    PASSWORD = "7eae7644"

    # Get user input
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    # Verify credentials
    if username == LOGIN_ID and password == PASSWORD:
        return True
    else:
        return False

# Define functions to display different pages
def network_audit():
    st.title("Network Audit")
    menu = ["Firewall Stats", "Open Port Logs", "Network Stats"]
    choice = st.sidebar.selectbox("Select an option", menu)

    # Display selected sub-page
    if choice == "Firewall Stats":
        st.subheader("Firewall Stats")
        csv_link = "https://example.com/firewall_stats.csv" # Replace with actual link to CSV file
        df = pd.read_csv(csv_link)

        # Create a dictionary to map boolean values to checkmark or cross symbols
        status_dict = {True: "✅", False: "❌"}

        # Replace the boolean values with checkmark or cross symbols
        df["Enabled"] = df["Enabled"].map(status_dict)

        # Table BG
        st.markdown(
            '<style>div.row-widget.stRadio > div{background-color: #f4f4f4}</style>',
            unsafe_allow_html=True,
        )

        # Display table
        st.write(df)

    elif choice == "Open Port Logs":
        st.subheader("Open Port Logs")
        st.write("Coming soon...")

    elif choice == "Network Stats":
        st.subheader("Network Stats")
        st.write("Coming soon...")

def os_audit():
    st.title("OS Audit")
    menu = ["OS Details", "System Version", "Peripheral Devices"]
    choice = st.sidebar.selectbox("Select an option", menu)

    # Display selected sub-page
    if choice == "OS Details":
        st.subheader("OS Details")
        st.write("Coming soon...")

    elif choice == "System Version":
        st.subheader("System Version")
        st.write("Coming soon...")

    elif choice == "Peripheral Devices":
        st.subheader("Peripheral Devices")
        st.write("Coming soon...")

def vulnerability_assessment():
    st.title("Vulnerability Assessment")
    st.write("Coming soon...")

def malware_logs():
    st.title("Malware Logs")
    st.write("Coming soon...")

# Define main function to run the app
def main():
    # Authenticate user
    authenticated = login()

    # If authentication successful, display app
    if authenticated:
        st.sidebar.success("Logged in as securitybulls")

        # Display sidebar menu
        st.sidebar.title("Navigation")
        menu = ["Network Audit", "OS Audit", "Vulnerability Assessment", "Malware Logs"]
        choice = st.sidebar.selectbox("Select a page", menu)

        # Display selected page
        if choice == "Network Audit":
            network_audit()
        elif choice == "OS Audit":
            os_audit()
        elif choice == "Vulnerability Assessment":
            vulnerability_assessment()
        elif choice == "Malware Logs":
            malware_logs()
    else:
        st.sidebar.error("Incorrect username or password")

        # Display login button
        login_button = st.sidebar.button("Login")

        # If login button clicked, re-attempt authentication
        if login_button:
            authenticated = login()
            if authenticated
# Define main function to run the app
def main():
    # Authenticate user
    authenticated = login()

    # If authentication successful, display app
    if authenticated:
        st.sidebar.success("Logged in as securitybulls")

        # Display sidebar menu
        st.sidebar.title("Navigation")
        menu = ["Network Audit", "OS Audit", "Vulnerability Assessment", "Malware Logs"]
        choice = st.sidebar.selectbox("Select a page", menu)

        # Display selected page
        if choice == "Network Audit":
            network_audit()
        elif choice == "OS Audit":
            os_audit()
        elif choice == "Vulnerability Assessment":
            vulnerability_assessment()
        elif choice == "Malware Logs":
            malware_logs()
    else:
        st.sidebar.error("Incorrect username or password")

        # Display login button
        login_button = st.sidebar.button("Login")

        # If login button clicked, re-attempt authentication
        if login_button:
            authenticated = login()
            if authenticated:
                st.sidebar.success("Logged in as securitybulls")

                # Display sidebar menu
                st.sidebar.title("Navigation")
                menu = ["Network Audit", "OS Audit", "Vulnerability Assessment", "Malware Logs"]
                choice = st.sidebar.selectbox("Select a page", menu)

                # Display selected page
                if choice == "Network Audit":
                    network_audit()
                elif choice == "OS Audit":
                    os_audit()
                elif choice == "Vulnerability Assessment":
                    vulnerability_assessment()
                elif choice == "Malware Logs":
                    malware_logs()

if __name__ == "__main__":
    main()
