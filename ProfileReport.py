# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 00:15:54 2023

@author: pipsi
"""

import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('C:/Users/pipsi/OneDrive/Desktop/Python_Projects/Equity_Data.csv')
profile = ProfileReport(df,title='Distict Data Profile')

profile.to_file('District_Enrollment_Analysis.html')