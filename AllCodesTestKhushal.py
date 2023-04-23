import streamlit as st
import pandas as pd

# Define login credentials
LOGIN_ID = "securitybulls"
PASSWORD = "7eae7644"

# Define sub-page names
NETWORK_AUDIT = "Network Audit"
OS_AUDIT = "OS Audit"
VULNERABILITY_ASSESSMENT = "Vulnerability Assessment"
MALWARE_LOGS = "Malware Logs"

# Define sub-page options for each page
SUB_PAGES = {
    NETWORK_AUDIT: ["Firewall Stats", "Open Port Logs", "Network Stats"],
    OS_AUDIT: ["OS Details", "System Version", "Peripheral Devices"],
    VULNERABILITY_ASSESSMENT: ["Assessment 1", "Assessment 2", "Assessment 3"],
    MALWARE_LOGS: ["Log 1", "Log 2", "Log 3"]
}

# Define function to authenticate user
def login():
    st.title("Login")

    # Get login credentials from user
    login_id = st.text_input("Login ID")
    password = st.text_input("Password", type="password")

    # Check if credentials are valid
    if login_id == LOGIN_ID and password == PASSWORD:
        # Return True to indicate authentication success
        return True
    else:
        # Return False to indicate authentication failure
        return False

# Define function to display Network Audit sub-pages
def network_audit():
    st.title("Network Audit")

    # Display sidebar with sub-page options
    sub_page = st.sidebar.selectbox("Select a sub-page", SUB_PAGES[NETWORK_AUDIT])

    # Display selected sub-page
    if sub_page == "Firewall Stats":
        st.title("Firewall Stats")
        csv_link = "https://example.com/firewall_stats.csv" # Replace with actual CSV link
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
    elif sub_page == "Open Port Logs":
        st.title("Open Port Logs")
        # Add code to display Open Port Logs
    elif sub_page == "Network Stats":
        st.title("Network Stats")
        # Add code to display Network Stats

# Define function to display OS Audit sub-pages
def os_audit():
    st.title("OS Audit")

    # Display sidebar with sub-page options
    sub_page = st.sidebar.selectbox("Select a sub-page", SUB_PAGES[OS_AUDIT])

    # Display selected sub-page
    if sub_page == "OS Details":
        st.title("OS Details")
        # Add code to display OS Details
    elif sub_page == "System Version":
        st.title("System Version")
        # Add code to display System Version
    elif sub_page == "Peripheral Devices":
        st.title("Peripheral Devices")
        # Add code to display Peripheral Devices

# Define function to display Vulnerability Assessment sub-pages
def vulnerability_assessment():
    st.title("Vulnerability Assessment")

    # Display sidebar with sub-page options
    sub_page = st.sidebar.selectbox("Select a sub-page", SUB_PAGES[VULNERABILITY_ASSESSMENT])

    # Display selected sub-page
    if sub_page == "Assessment 1":
        st.title("Assessment 1")
        # Add code to display Assessment 1
    elif sub_page == "Assessment 2":
        st.title("Assessment 2")
        # Add code to display Assessment 2
    elif sub_page == "Assessment 3":
        st.title("Assessment 3")
        # Add code to display Assessment 3

# Define function to display Malware Logs sub-pages
def malware_logs():
    st.title("Malware Logs")

    # Display sidebar with sub-page options
    sub_page = st.sidebar.selectbox("Select a sub-page", SUB_PAGES[MALWARE_LOGS])

    # Display selected sub-page
    if sub_page == "Log 1":
        st.title("Log 1")
        # Add code to display Log 1
    elif sub_page == "Log 2":
        st.title("Log 2")
        # Add code to display Log 2
    elif sub_page == "Log 3":
        st.title("Log 3")
        # Add code to display Log 3

# Define function to run the app
def run_app():
    # Authenticate user
    authenticated = login()

    if authenticated:
        # Define left sidebar options
        options = [NETWORK_AUDIT, OS_AUDIT, VULNERABILITY_ASSESSMENT, MALWARE_LOGS]

        # Display sidebar with options
        page = st.sidebar.selectbox("Select a page", options)

        # Display selected page
        if page == NETWORK_AUDIT:
            network_audit()
        elif page == OS_AUDIT:
            os_audit()
        elif page == VULNERABILITY_ASSESSMENT:
            vulnerability_assessment()
        elif page == MALWARE_LOGS:
            malware_logs()

# Run the app
run_app()
