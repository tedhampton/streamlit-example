# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:54:56 2023

@author: pipsi
"""
import streamlit as st
import pandas as pd
import streamlit_pandas as sp

#@st.cache(allow_output_mutation=True)

#@st.cache(allow_output_mutation=True)

st.cache_data()

def load_data():
    df = pd.read_csv("C:/Users/pipsi/OneDrive/Desktop/Python_Projects/Equity_Data.csv")

    df = pd.DataFrame(df)
    
    return df



df = load_data()
#st.write(df)

st.markdown('###')
st.markdown('###')


create_data = { 
                "ID": " ",
                "NETWORK": "multiselect",
                "SCHOOL": "multiselect",
                "GENDER": "multiselect",
                "YEAR": "select",
                "WEEK": "select",
                "GROUP": "multiselect"
            
                }





all_widgets = sp.create_widgets(df, create_data )

res=sp.filter_df(df, all_widgets)

st.markdown('### District Schools Filtered')

st.dataframe(res)





