
import pandas as pd
import numpy as np
import streamlit as st

# Data import & columns
df = pd.read_csv('C:/Users/pipsi/OneDrive/Desktop/Python_Projects/Equity_Data.csv')

#df['90s'] = df['minutes']/90

calc_elements = ['DAYS_PRESENT', 'RATE', 'COUNT']

#or each in calc_elements:
#    df[f'{each}_p90'] = df[each] / df['90s']

groups = list(df['GROUP'].drop_duplicates())
schools = list(df['SCHOOL'].drop_duplicates())
network = list(df['NETWORK'].drop_duplicates())
gender = list(df['GENDER'].drop_duplicates())


# App

# Sidebar - title & filters
st.sidebar.markdown('### Data Filters')

group_choice = st.sidebar.multiselect(
    "Group:", groups, default=groups)

gender_choice = st.sidebar.multiselect(
    "Gender:", gender, default=gender)

network_choice = st.sidebar.multiselect(
    "Network:", network, default=network)

#school_choice = st.sidebar.multiselect(
#   "Schools:", schools, default=schools)


#rate_choice = st.sidebar.slider(
#    'rate Range:', min_value=0.0, max_value=100.0, step=1.0, value=0.0)

df = df[df['GROUP'].isin(group_choice)]
df = df[df['GENDER'].isin(gender_choice)]
df = df[df['NETWORK'].isin(network_choice)]
#df = df[df['SCHOOL'].isin(school_choice)]
#df = df[df['RATE'] < rate_choice]

# Main
st.title(f"CPS Schools Network Analysis")

# Main - dataframes
st.markdown('### District Schools')

st.dataframe(df.sort_values('SCHOOL',
             ascending=True).reset_index(drop=True))

 



