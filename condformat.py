# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:31:17 2023

@author: pipsi
"""

import pandas as pd
import numpy as np
import streamlit as st

# Data import & columns
df = pd.read_csv('C:/Users/pipsi/OneDrive/Desktop/Python_Projects/Equity_Data.csv')


def color_df(val):
    if val > .850:
        color = '#b5edb2'
    else:
        color = '#f7cbc3'
    return f'background-color: {color}'
    

# Main
st.title(f"CPS Schools Network Analysis")

# Main - dataframes
st.markdown('### District Schools')

st.dataframe(df.style.applymap(color_df, subset=['RATE']))

 
      

