import pickle
from pathlib import Path
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth
import yaml
from streamlit_option_menu import option_menu
# --- USER AUTHENTICATION ---
with open('/Users/aishworyann/Desktop/Streamlit Authenticator/config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')
def firewall():
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

if authentication_status == False:
    st.error("Username/password is incorrect")
if authentication_status == None:
    st.warning("Please enter your username and password")
if authentication_status:
    # ---- SIDEBAR ----
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    with st.sidebar:
        selected = option_menu(
            menu_title= "Dashboard",
            options=["Home", "Analytics", "About"],
            icons=["house", "activity","envelope"],
            menu_icon="cast",
            default_index=0,
        )
    if selected== "Home":
        st.title(f"{selected}")
    if selected == "Analytics":
        st.title(f"{selected}")
        firewall()
        
    if selected == "About":
        st.title(f"{selected}")

