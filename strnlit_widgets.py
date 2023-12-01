# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 21:37:50 2023

@author: pipsi
"""

import streamlit as st

st.set_page_config(page_title = "Example Streamlit App")
st.header("Welcome!")

c1, c2, c3 = st.columns(3)

c1.metric(label='VIEWS', value= 12400, delta=4400)
c2.metric(label='WATCH TIME', value= 757.5, delta=250)
c3.metric(label='SUBSCRIBERS', value= 193, delta=0)

#c1.style_metric_card(border_left_color='#1E1E1E')
#c2.style_metric_card(border_left_color='#1E1E1E')
#c3.style_metric_card(border_left_color='#1E1E1E')



# slider widget
c1.markdown(" ")
num = c1.slider("Select a number", 1, 10)

# display the selected number
st.write("You selected:", num)


# checkbox
c2.markdown(" ")
if c2.checkbox("Show message"):
    c2.write("Hello!")

# checkbox
c3.markdown(" ")
c3.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")


# selectbox

option = st.selectbox("Select an option", ["A", "B", "C"])
st.write("You selected:", option) # display the selected option




