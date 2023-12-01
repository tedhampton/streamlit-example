# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:26:14 2023

@author: pipsi
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data in dict for dataframe.

col1, col2 = st.columns([6,5])

excel_file = 'C:/Users/pipsi/OneDrive/Desktop/Python_Projects/network_counts.xlsx'
sheet_name = 'Sheet1'

data = pd.read_excel(excel_file,
                  sheet_name=sheet_name,
                  usecols='A:B', 
                  header=0)


# Build df.
df = pd.DataFrame(data)
col1.dataframe(df, use_container_width=True)


sel_Network = col2.selectbox('**Select Network**', df.Network)
fil_df = df[df.Network == sel_Network]  # filter

# Build a new df based from filter.
new_df = pd.melt(fil_df, id_vars=['Network'], var_name="feature",
                 value_vars=['Count'])

logy = True  # to make small values visible
textauto = True  # to write plot label
title = f'network: {sel_Network}'
fig = px.bar(new_df, x='feature', y='value',
             height=300, log_y=logy, text_auto=textauto,
             title=title)

with col2.expander('**Network Info**', expanded=True):
    st.plotly_chart(fig, use_container_width=True)
    