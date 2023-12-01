# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 22:43:10 2023

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

 
#df = pd.read_csv('C:/Users/pipsi/OneDrive/Desktop/Python_Projects/values.csv')



conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=HELLACIOUSQUE;'
                     'Database=MyDatasets;'
                     'Trusted_Connection=yes;')

pd.set_option("max_colwidth", None)

df = pd.read_sql_query("""
                      SELECT *
                     FROM [MyDatasets].[dbo].[IPEDS_Data]
                     WHERE [Historically Black College or University] = 'Yes'
                     AND [Enrolled total] IS NOT NULL
                     AND [lat] IS NOT NULL
                     AND [lat] NOT IN (' ')
                     AND [long] IS NOT NULL
                     AND [long] NOT IN (' ')
                       """, conn)
                        
                     

st.dataframe(df)

