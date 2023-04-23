import streamlit as st

# Login credentials
LOGIN_ID = "securitybulls"
PASSWORD = "7eae7644"

# Define function for login page
def login():
    st.title("Login")

    # Get login details from user
    login_id = st.text_input("Login ID")
    password = st.text_input("Password", type="password")

    # Check if login details are correct
    if login_id == LOGIN_ID and password == PASSWORD:
        st.success("Login successful!")
        return True
    else:
        st.error("Incorrect login details. Please try again.")
        return False

# Define function for network audit page
def network_audit():
    st.title("Network Audit")
    sub_page = st.sidebar.radio("Select Sub-Page", ["Firewall Stats", "Open Port Logs", "Network Stats"])

    if sub_page == "Firewall Stats":
        st.title("Firewall Status")

        # Replace the link with the actual link to the CSV file
        csv_link = "https://example.com/firewall_stats.csv"
        df = pd.read_csv(csv_link)

        # Create a dictionary to map boolean values to checkmark or cross symbols
        status_dict = {True: "✅", False: "❌"}

        # Replace the boolean values with checkmark or cross symbols
        df["Enabled"] = df["Enabled"].map(status_dict)

        #Table BG
        st.markdown(
            '<style>div.row-widget.stRadio > div{background-color: #f4f4f4}</style>',
            unsafe_allow_html=True,
        )

        # Display table
        st.write(df)

    elif sub_page == "Open Port Logs":
        st.title("Open Port Logs")
        # Code to display open port logs goes here

    elif sub_page == "Network Stats":
        st.title("Network Stats")
        # Code to display network stats goes here

# Define function for OS audit page
def os_audit():
    st.title("OS Audit")
    sub_page = st.sidebar.radio("Select Sub-Page", ["OS Details", "System Version", "Peripheral Devices"])

    if sub_page == "OS Details":
        st.title("OS Details")
        # Code to display OS details goes here

    elif sub_page == "System Version":
        st.title("System Version")
        # Code to display system version goes here

    elif sub_page == "Peripheral Devices":
        st.title("Peripheral Devices")
        # Code to display peripheral devices goes here

# Define function for vulnerability assessment page
def vulnerability_assessment():
    st.title("Vulnerability Assessment")
    # Code to perform vulnerability assessment goes here

# Define function for malware logs page
def malware_logs():
    st.title("Malware Logs")
    # Code to display malware logs goes here

# Define the main function for the Streamlit app
def main():
    if login():
        # Create a sidebar with options to navigate to different pages
        st.sidebar.title("Navigation")
        pages = ["Network Audit", "OS Audit", "Vulnerability Assessment", "Malware Logs"]
        page = st.sidebar.radio("Go to", pages)

        # Call the appropriate function based on the selected page
        if page == "Network Audit":
            network_audit()
        elif page == "OS Audit":
            os_audit()
        elif page == "Vulnerability Assessment":
            vulnerability_assessment()
        elif page == "Malware Logs":
            malware_logs()

if __name__ == "__main__":
    main()
