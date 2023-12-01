# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 22:44:58 2023

@author: pipsi
"""

import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

@st.cache_data()
def load_data():
    data = pd.read_csv('C:/Users/pipsi/OneDrive/Desktop/Python_Projects/Equity_Data.csv')
    return data

data = load_data()

AgGrid(data, height=900, width= 1100)

