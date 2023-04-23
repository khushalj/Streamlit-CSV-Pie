import streamlit as st
import pandas as pd
import altair as alt

# Load the CSV file
file = st.file_uploader("Upload CSV file", type=["csv"])
if file:
    df = pd.read_csv(file)

    # Create a bar chart of InterfaceAlias and Source
    chart = alt.Chart(df).mark_bar().encode(
        x='InterfaceAlias',
        y='count()',
        color='Source'
    ).properties(
        width=600,
        height=400
    )
    st.altair_chart(chart)

    # Create a table of statistics for each InterfaceAlias
    interfaces = df['InterfaceAlias'].unique()
    for interface in interfaces:
        st.write('## ' + interface)
        subset = df[df['InterfaceAlias'] == interface]
        subset = subset.drop(columns=['ifAlias', 'ifDesc', 'Caption', 'Description', 'ElementName', 'InstanceID', 'InterfaceDescription', 'Name', 'Source', 'SystemName'])
        st.write(subset)
