# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 23:29:22 2023

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

    st.dataframe(df)
    #st.table(df)
    

