# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 23:02:25 2023

@author: pipsi
"""
import streamlit as st    
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd



df = pd.read_csv('C:/Users/pipsi/OneDrive/Desktop/Python_Projects/employees.csv')
pd.set_option("max_colwidth", None)

gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=True, groupable=True)

sel_mode = st.radio('Selection type', options=['single','multiple'])
gd.configure_selection(selection_mode=sel_mode, use_checkbox=True)

grid_option = gd.build()
grid_table = AgGrid(df, 
                    gridOptions=grid_option, 
                    update_mode=GridUpdateMode.SELECTION_CHANGED,
                    height=700,
                    allow_unsafe_jscode=True,
                    theme='balham'
                    )

sel_row = grid_table["selected_rows"]

st.subheader("Output Table")


st.dataframe(sel_row)

