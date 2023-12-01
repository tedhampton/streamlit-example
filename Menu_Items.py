# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:49:04 2023

@author: pipsi
"""

import streamlit as st
from streamlit_option_menu import option_menu



with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu", 
        options=["Home","About","Projects","Contact"],
        icons=["house","person","book","envelope"],
        menu_icon="cast",
        default_index=0,
        orientation=0
        )
    
    
    
if selected =="Home":
    st.title(f'You have selected {selected}')
if selected =="About":
    st.title(f'You have selected {selected}')
if selected =="Projects":
    st.title(f'You have selected {selected}')
if selected =="Contact":
    st.title(f'You have selected {selected}')