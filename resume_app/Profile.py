# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 00:51:29 2023

@author: pipsi
"""

import streamlit as st

st.set_page_config(
    page_title="RESUME",
    page_icon="👋",
)

##st.title("Profile")
st.sidebar.success("Select a page above.")

#col1.markdown('My Profile')
st.title("Theodore E. Hampton")
st.markdown('Data Science Background')
st.write("Act as the primary liaison between the campus and the VP Technology/ Infrastructure to ensure reporting-relevant work streams are synchronized between departments. Design, develop, maintain, revise, and quality check multiple reports for a variety of metrics and stakeholder groups in the Microsoft BI platform, Power Query, and Microsoft Excel. Manage governance and quality assurances processes as they relate to report design and content. Gather and translate business requirements to scope report designs.") 
st.write("Worked directly with the Director of Data Science and various academic stakeholders to iteratively examine, evaluate, and develop reporting needs. Communicate reporting changes, enhancements, and modifications verbally or through written documentation to management and other team members. Develop, document, and maintain detailed query specifications and report inventory related to report content. Use Oracle and SQL Server data warehouse architecture design for self-service reporting.")

col1, col2, col3 = st.columns([2,2,1])

col1.markdown('Education')
with col1.expander("Click to read more!"):
      st.write("Master of Science in Computer Science: DePaul University - Chicago, IL, June 2005")
      st.write("Master of Education in Instructional Technologies: University of Illinois - Urbana-Champaign, IL, January 1995")
      st.write("Bachelor of Science in Business Administration: University of Illinois - Urbana-Champaign, IL, September 1991")

col2.markdown('Related Skills')
with col2.expander("Click to read more!"):
      st.write("Languages: Python, R, C#, SQL/TSQL, DAX, MDX, HTML, CSS, ASP, XML, JavaScript, JSON, jQuery")
      st.write("Software: Power BI, Tableau, Excel BI: PowerQuery, M-Language, Azure ML Studio, Rapid Miner, Google Data Studio")
      st.write("Databases: Microsoft SQL Server, AWS, MySQL Workbench, Oracle, Access, Postgres")
      st.write("Data Science Platforms: Anaconda, Spyder, Jupyter Notebooks, Datalore, R-Studio, VSCode")