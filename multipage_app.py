# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 23:32:16 2023

@author: pipsi
"""

#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px

st.set_page_config(layout="wide")


# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a (CSV) file')

def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())

def displaybar():
    
    st.header('Bar Graph')
    st.bar_chart(df, x='Location', y='Salary')
    



# Add a title and intro text
st.title('Regional Salary Data Explorer')
st.text('This is a web app to allow for the exploration of Regional Salary Data')

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing Salary data')

#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 
                                                                'Data Summary', 
                                                                'Data Header', 
                                                                'Bar Graph']
                           )

# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file)
    


# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'Bar Graph':
    displaybar()

    
