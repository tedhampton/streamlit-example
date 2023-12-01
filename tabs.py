# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 18:50:48 2023

@author: pipsi
"""

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.graph_objects as go

st.title("Dublin Ireland")
st.markdown("The dashboard show the geo-spatial data for Dublin")
st.sidebar.title("Side Bar")


dataset1 = pd.read_csv("C:/Users/pipsi/OneDrive/Desktop/Python_Projects/employees.csv")
dataset2 = pd.read_csv("C:/Users/pipsi/OneDrive/Desktop/Python_Projects/dublin.csv")
dataset3 = pd.read_csv("C:/Users/pipsi/OneDrive/Desktop/Python_Projects/fpldata.csv") 

import streamlit as st


image1 = Image.open('C:/Users/pipsi/OneDrive/Pictures/Black Panther Party (4).jpg')
image2 = Image.open('C:/Users/pipsi/OneDrive/Pictures/Black Panther Party (2).jpg')
image3 = Image.open('C:/Users/pipsi/OneDrive/Pictures/Black Panther Party (5).jpg')

#st.image(image, caption='Sunrise by the mountains')


tab1, tab2, tab3, tab4 = st.tabs(["Tab 1", "Tab2", "Tab3", "Tab4"])

#tab1.table(dataset1)
#tab2.table(dataset2)
tab4.table(dataset3)
tab3.image(image3)
tab2.image(image2)
tab1.image(image1)




