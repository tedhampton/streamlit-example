# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 00:33:31 2023

@author: pipsi
"""

import streamlit as st
import pandas as pd
import pyodbc 

 
## Create a sample DataFrame with latitude and longitude values
conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=HELLACIOUSQUE;'
                     'Database=MyDatasets;'
                     'Trusted_Connection=yes;')

df = pd.read_sql_query("""
                      SELECT 
                      [lat]
                      ,[lon]
                      FROM [MyDatasets].[dbo].[Locations]
  
                       """, conn)
 
    
 
    
 
## Create a map with the data
st.map(df, zoom=2)

col1, col2, col3 = st.columns([3,5,4])





col1.markdown("WHAT'S NEW!")
col1.markdown('Here is some content and info on the App')
with col1.expander("Click to read more!"):
      st.write("Streamlit is more than just a way to make data apps, it’s also a community of creators that share their apps and ideas and help each other make their work better.")


col2.markdown('WELCOME TO MY APP')
col2.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
with col2.expander("Click to read more!"):
      st.write("Streamlit is more than just a way to make data apps, it’s also a community of creators that share their apps and ideas and help each other make their work better.")