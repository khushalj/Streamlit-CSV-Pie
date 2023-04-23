import streamlit as st
import pandas as pd

def firewall_stats():
    st.title("Firewall Status")

    # Upload CSV
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

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

if __name__ == "__main__":
    st.set_page_config(page_title="Security Bulls App")

    # Login Page
    login_id = st.secrets["login_id"]
    password = st.secrets["password"]
    user_input_id = st.text_input("Enter Login ID")
    user_input_password = st.text_input("Enter Password", type="password")
    if st.button("Login"):
        if user_input_id == login_id and user_input_password == password:
            st.success("Logged In!")
            menu = ["Network Audit", "OS Audit", "Vulnerability Assessment", "Malware Logs"]
            choice = st.sidebar.selectbox("Select an option", menu)
            if choice == "Network Audit":
                network_audit_menu = ["Firewall Stats", "Open Port Logs", "Network Stats"]
                network_audit_choice = st.sidebar.selectbox("Select a subpage", network_audit_menu)
                if network_audit_choice == "Firewall Stats":
                    firewall_stats()
            elif choice == "OS Audit":
                os_audit_menu = ["OS Details", "System Version", "Peripheral Devices"]
                os_audit_choice = st.sidebar.selectbox("Select a subpage", os_audit_menu)
                if os_audit_choice == "Firewall Stats":
                    # Write code for OS Details subpage here
                    pass
        else:
            st.error("Invalid Login ID or Password")
                        elif choice == "Vulnerability Assessment":
                # Write code for Vulnerability Assessment page here
                pass
            elif choice == "Malware Logs":
                # Write code for Malware Logs page here
                pass
    else:
        pass

