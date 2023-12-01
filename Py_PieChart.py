# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 15:01:29 2020

@author: Owner
"""
#import numpy as np
import matplotlib.pyplot as plt

labels = ('Compter Science', 'Foreign Language','Analytical Chemistry', 'Education', 'Humanties','Physics', 'Biology', 'Statistics', 'Engineering')

sizes = [21, 10, 7, 7, 8, 9, 20, 15, 13]

colors = ['yellowgreen', 'gold', 'lightskyblue','lightcoral','red', 'purple', '#f280de', 'orange', 'green']

explode = (0,0,0,0,0,0,0,0,0.1)
plt.pie(sizes, explode=explode, labels=labels,
autopct='%1.1f%%', colors=colors)
plt.axis('equal')
plt.show()