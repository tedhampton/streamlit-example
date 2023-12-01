# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 01:08:12 2023

@author: pipsi
"""

import asyncio
from contextlib import contextmanager
import streamlit as st

# Create a context manager to run an event loop
@contextmanager
def setup_event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        yield loop
    finally:
        loop.close()
        asyncio.set_event_loop(None)

# Use the context manager to create an event loop
with setup_event_loop() as loop:
    import sketch

# Now you can use the 'sketch' library in your Streamlit app
st.write("The 'sketch' library has been successfully imported.")
