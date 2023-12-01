# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 14:42:38 2023

@author: pipsi
"""

import streamlit as st
import pandas as pd
import pyodbc 
import pandasql as ps
from   pandasql import sqldf
import sqlalchemy as sal
from   sqlalchemy import create_engine
import numpy as np
import time
import plotly.express as px
from streamlit_folium import st_folium
 
#df = pd.read_csv('C:/Users/pipsi/OneDrive/Desktop/Python_Projects/values.csv')



conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=HELLACIOUSQUE;'
                     'Database=MyDatasets;'
                     'Trusted_Connection=yes;')

df = pd.read_sql_query("""
                      SELECT 
                      [Name]
                     ,[State abbreviation] as 'State'
                     ,CAST([long] AS float) AS'lon'
                     ,CAST([lat] AS float) AS 'lat'
                     ,CAST([Enrolled total] AS numeric) AS 'Enrolled'
                     FROM [MyDatasets].[dbo].[IPEDS_Data]
                     WHERE [Historically Black College or University] = 'Yes'
                     AND [Enrolled total] IS NOT NULL
                     AND [lat] IS NOT NULL
                     AND [lat] NOT IN (' ')
                     AND [long] IS NOT NULL
                     AND [long] NOT IN (' ')
                       """, conn)
                        
                     

st.dataframe(df)



st.write('Map data')

data_of_map = pd.DataFrame(df, 
                           columns = ['lat', 'lon'], 
                           
                           )
st.map(data_of_map)


st.header("Bar Chart")
st.bar_chart(df,
    x='Name',
    y='Enrolled',
    color=['#000FFF']  # Optional
)
