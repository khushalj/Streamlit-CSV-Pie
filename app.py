import streamlit as st
import pandas as pd
import plotly.express as px

# Define the Streamlit app
def main():
    # Set the page title
    st.title("Port State Analysis")

    # Allow the user to upload a CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(uploaded_file)

        # Calculate the percentage of open and closed ports
        total_ports = len(df)
        open_ports = len(df[df['state'] == 'open'])
        close_ports = total_ports - open_ports
        open_percentage = round(open_ports / total_ports * 100, 2)
        close_percentage = round(close_ports / total_ports * 100, 2)

        # Create a pie chart to display the data
        data = {'State': ['Open', 'Close'], 'Percentage': [open_percentage, close_percentage]}
        fig = px.pie(data, values='Percentage', names='State')

        # Set the chart title and labels
        fig.update_layout(title="Port State Analysis", xaxis_title="State", yaxis_title="Percentage")

        # Display the pie chart
        st.plotly_chart(fig)

# Run the Streamlit app
if __name__ == "__main__":
    main()
