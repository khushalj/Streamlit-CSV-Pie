import streamlit as st
import pandas as pd
def main():
    st.title("Firewall Status")

    # Upload CSV
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        for i in range(len(df)):
            name = df.iloc[i]['Name']
            enabled = df.iloc[i]['Enabled']
            if enabled:
                st.write(name + " ✅")
            else:
                st.write(name + " ❌")
if __name__ == "__main__":
    main()
