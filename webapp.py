# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 01:08:43 2023

@author: pipsi
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

st.set_page_config(page_title='My First Web App')

excel_file = 'C:/Users/pipsi/OneDrive/Desktop/Python_Projects/equity.xlsx'
sheet_name = 'equity'

df = pd.read_excel(excel_file,
                  sheet_name=sheet_name,
                  usecols='B:E,H,K', 
                  header=0)

df.dropna(inplace=True)    





col1, col2, col3 = st.columns([1,2,1])

col1.markdown("WHAT'S NEW!")
col1.markdown('Here is some content and info on the App')
with col1.expander("Click to read more!"):
      st.write("Streamlit is more than just a way to make data apps, it’s also a community of creators that share their apps and ideas and help each other make their work better.")


col2.markdown('WELCOME TO MY APP')
col2.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
with col2.expander("Click to read more!"):
      st.write("Streamlit is more than just a way to make data apps, it’s also a community of creators that share their apps and ideas and help each other make their work better.")



    
with st.expander("Click to read more!"):
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. ")

with st.expander("View Table!"): 
        st.dataframe(df)
        
col3.metric(label="TODAY'S TEMP", value="27 °C", delta="3 °C")
    
with col3.expander("Click to read more!"):
      st.write("Streamlit is more than just a way to make data apps, it’s also a community of creators that share their apps and ideas and help each other make their work better.")
      


