# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 01:02:43 2023

@author: pipsi
"""

import streamlit as st

st.title("Contact")

st.markdown('Please feel free to reach out. I welcome new opportunities')
with st.expander("Click to Contact Information!"):
      st.header("Theodore E. Hampton")
      st.write("LinkedIn Profile [LinkedIn](http://linkedin.com/in/tedhampton)")
      st.markdown('<a href="tedhampton@gmail.com">tedhampton@gmail.com</a>', unsafe_allow_html=True)
      st.write("(773) 807-1236")
      st.write("Chicago, IL 60636")
     