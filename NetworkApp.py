# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:47:06 2023

@author: pipsi
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from PIL import Image




st.set_page_config(page_title='CPS District Rates')
st.header('2022 Attendance Rates')
st.subheader('View of schools by network attendance rates')

excel_file = 'C:/Users/pipsi/OneDrive/Desktop/Python_Projects/equity.xlsx'
sheet_name = 'equity'

df = pd.read_excel(excel_file,
                                   sheet_name=sheet_name,
                                   usecols='A:K', 
                                   header=0)

#df['COUNT'].map('{:,d}'.format)
dataframe = pd.DataFrame(df,
                         columns = ['NETWORK', 
                                    'SCHOOL', 
                                    'GENDER',
                                    'SUBGROUP', 
                                    'RATE']
                         ) 

N17 = dataframe.query("NETWORK == 'Network 17' & SUBGROUP == 'Black' ")

schoolcount = df['SCHOOL'].nunique()
present_avg = df['DAYS_PRESENT'].mean().round(1)
member_avg = df['DAYS_MEMBERSHIP'].mean().round(1)
avg_rate = df['RATE'].mean().round(4)
total = df['COUNT'].sum()


c1, c2, c3, c4, c5 = st.columns(5)

st.markdown(
    """
<style>
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: red;
}
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div p {
   font-size: 100% !important;
}
</style>
""",
    unsafe_allow_html=True,)


c1.metric(label='Count of Schools', value=schoolcount, delta=0)
c2.metric(label='Avg Attenedance', value= present_avg, delta=5)
c3.metric(label='Avg Membership', value= member_avg, delta=5)
c4.metric(label='Avg Rate', value= avg_rate , delta=0)
c5.metric(label='Total Enrollment', value= total, delta=0)

c1.markdown(" ")

st.dataframe(df)

pie_chart = px.pie(df,
                   title='Network Counts',
                   values='COUNT',
                   names='NETWORK')

st.plotly_chart(pie_chart)

st.dataframe(N17)









