import streamlit as st
import csv

# Title of the app
st.title('Bar Graph from CSV')

# Function to read CSV data
def read_csv(file_path):
    data = {'column_name': [], 'count': []}
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data['column_name'].append(row['column_name'])
            data['count'].append(int(row['count']))
    return data

# Read the CSV data
data = read_csv('data.csv')

# Create bar chart
st.bar_chart(data)
