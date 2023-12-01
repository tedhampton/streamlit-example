# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 09:50:45 2023

@author: pipsi
"""


import streamlit as st
import pandas as pd
import numpy as np
from bokeh.plotting import figure

## Streamlit only supports Bokeh version 2.4.3, but you have version 3.2.1 installed.

df = pd.read_csv('C:/Users/pipsi/OneDrive/Desktop/Python_Projects/network_counts.csv')

x = df['Network']
y = df['Count']

p = figure(
    title='simple line example',
    x_axis_label='Networks',
    y_axis_label='Enrollment')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)
