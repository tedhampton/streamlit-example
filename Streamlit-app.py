# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

excel_file = 'C:/Users/pipsi/OneDrive/Desktop/Python_Projects/equity.xlsx'
sheet_name = 'equity'

df = pd.read_excel(excel_file,
                  sheet_name=sheet_name,
                  usecols='A:K', 
                  header=0)


st.set_page_config(page_title='My Web App')



col1, col2, col3 = st.columns([1,2,1])

col1.markdown('WELCOME TO MY APP')
col1.markdown('Here is some content and info on the App')
with col1.expander("Click to read more!"):
      st.write("Streamlit is more than just a way to make data apps, it’s also a community of creators that share their apps and ideas and help each other make their work better.")

upload_pic = col2.file_uploader('Upload a pic')
camera_pic = col2.camera_input('Take a pic')

col2.success("Photo uploaded sucessfully")

progress_bar = col2.progress(0)

for perc_completed in range(100):
    time.sleep(0.03)
    progress_bar.progress(perc_completed +1)
    


with st.expander("Click to read more!"):
    st.write("Streamlit is more than just a way to make data apps, it’s also a community of creators that share their apps and ideas and help each other make their work better. Please come join us on the community forum. We love to hear your questions, ideas, and help you work through your bugs — stop by today! ")

with st.expander("View Table!"): 
        st.dataframe(df)
        
col3.metric(label="Todays Temprature", value="27 °C", delta="3 °C")
    
with col3.expander("Click to read more!"):
      st.write("Streamlit is more than just a way to make data apps, it’s also a community of creators that share their apps and ideas and help each other make their work better.")
      


df.dropna(inplace=True)    


        
        