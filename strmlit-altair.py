# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 01:18:56 2023

@author: pipsi
"""

import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

df = pd.DataFrame(
                np.random.rand(10, 4),
                columns= ["NO2","C2H5CH","VOC","CO"])
# generate a date range to be used as the x axis
df['date'] =  pd.date_range("2014-01-01", periods=10, freq="m")
df_melted = pd.melt(df,id_vars=['date'],var_name='parameter', value_name='value')
c = alt.Chart(df_melted, title='measure of different elements over time').mark_line().encode(
     x='date', y='value', color='parameter')

st.altair_chart(c, use_container_width=True)