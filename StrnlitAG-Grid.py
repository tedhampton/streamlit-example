# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 23:02:25 2023

@author: pipsi
"""

from st_aggrid import AgGrid
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(df)
