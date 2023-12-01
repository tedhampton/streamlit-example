# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 19:37:07 2023

@author: pipsi
"""

import flet as ft

def main(page: ft.page):
    textField = ft.TextField()
    addButton = ft.ElevatedButton(text="Add")
    
    page.add(textField, addButton)
    
ft.app(target=main, view=ft.WEB_BROWSER)