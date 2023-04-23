import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Peripherals Status")

    filename = "PeripheralsAndAdaptersReport.csv"
    df = pd.read_csv(filename)
    status_dict = {"OK": "✅", "ERROR": "❌"}
    df["Status"] = df["Status"].map(status_dict)

    st.markdown(
        '<style>div.row-widget.stRadio > div{background-color: #f4f4f4}</style>',
        unsafe_allow_html=True,
    )
    st.write(df)

    total_class = len(df)
    system_adap = len(df[df['Class'] == 'System'])
    net_adap = total_class - system_adap
    System_percentage = round(system_adap/ total_class * 100, 2)
    Net_percentage = round( net_adap / total_class* 100, 2)

    data = {'Class': ['System', 'Net'], 'Percentage': [System_percentage, Net_percentage]}
    fig1 = px.pie(data, values='Percentage', names='Class', color_discrete_sequence=['yellow', 'teal'])

    st.plotly_chart(fig1)

if __name__ == "__main__":
    main()
