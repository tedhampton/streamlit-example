# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 01:55:19 2023

@author: pipsi
"""

import streamlit as st
import streamlit_pandas as sp
import pandas as pd

st.set_page_config(page_title='My Web App', layout="wide")

st.markdown('Here is some content and info on the App')

uploaded_file = st.sidebar.file_uploader("Choose a XLSX file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    
    
dataframe = pd.DataFrame(df,
                         columns = ['Institution', 
                                        'County', 
                                        'States',
                                        'Sector', 
                                        'Level',
                                        'Control',
                                        'Enrollment']
                             ) 
create_data = { 
               
                'States': "multiselect",
               
            
                }



all_widgets = sp.create_widgets(dataframe, create_data )

res=sp.filter_df(dataframe, all_widgets)

st.markdown('Search by School Criteria')

st.dataframe(res)


st.dataframe(df)

