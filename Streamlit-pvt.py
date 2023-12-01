# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 17:52:01 2023

@author: pipsi
"""

import streamlit as st
import streamlit.components.v1 as components
from pivottablejs import pivot_ui
import pandas as pd

df = pd.read_csv('C:/Users/pipsi/OneDrive/Desktop/Python_Projects/Equity_Data.csv')


t = pivot_ui(df)

with open(t.src) as t:
    components.html(t.read(), width=1900, height=1500, scrolling=True)