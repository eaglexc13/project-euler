# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 16:01:05 2018

@author: jamicali
"""

x = 1
for i in range(3,1002,2):
    x += 4*i**2 - 6*i + 6
print(x)