

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
from PIL import Image



st.header('_Streamlit_ is :blue[cool] :sunglasses:')

conn = pyodbc.connect('Driver={SQL Server};'
                     'Server=HELLACIOUSQUE;'
                     'Database=MyDatasets;'
                     'Trusted_Connection=yes;')

df = pd.read_sql_query("""
                       SELECT 
                      [Name] AS "Institution"
	                 ,[Control of institution] AS "Control"
	                 ,[Sector of institution] AS "Sector"
                     ,[Highest degree offered]	AS "Degree Awarded"
	                 ,[State abbreviation] AS "State"
                     ,[Longitude location of institution] AS "Long"
                     ,[Latitude location of institution] AS "Lat"
	                 ,[Historically Black College or University] AS "HBCU"
                     ,[Enrolled total]       
                     FROM [MyDatasets].[dbo].[IPEDS_Data]
                       
                       """, conn)

  
pie_chart = px.pie(df,
                   title='Degrees Awarded Count',
                   values='Enrolled total',
                   names='Degree Awarded'
                   )

pie_chart.update_layout(
                        ##autosize=False,
                        width=575,
                        height=500
                        )



col1, col2, col3 = st.columns([3,5,4])





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

with st.expander("View IPEDS Table"): 
        st.dataframe(df)
        
col3.metric(label="TODAY'S TEMP", value="27 °C", delta="3 °C")
         
with col3.expander("View Chart"): 
        st.plotly_chart(pie_chart)

