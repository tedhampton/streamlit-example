# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 21:50:51 2023

@author: pipsi
"""

import streamlit as st
import datetime
import time



#single-element container.
with st.empty():
    for seconds in range(20):
        st.write(f"⏳ {seconds} After 20 seconds display widgets")
        time.sleep(1)
    st.write("✔️ Display Widgets!")
st.markdown("***")

#button  
st.button("Reset", type="primary")

st.markdown("***")

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.markdown("***")

#Checkbox
agree = st.checkbox('I agree')

if agree:
    st.write('Great!')

st.markdown("***")

#Toggle   
on = st.toggle('Activate feature')

if on:
   st.write('Feature activated!')
    
st.markdown("***")
    
 #Radio Button   
genre = st.radio("What's your favorite movie genre",
[":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")

st.markdown("***")
    
#Select Box
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

st.markdown("***")

#Multiselect
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue','Orange'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

st.markdown("***")

#Slider Range
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (0.0, 50.0))
st.write('Values:', values)

st.markdown("***")

#Text Input
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

st.markdown("***")

#Date Input
d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)


























