# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 09:11:38 2018
PE 020
Find the sum of the digits in the number 100!
@author: Jimmy
"""

import math

s = 0
bigNum = math.factorial(100)
for char in str(bigNum):
    s += int(char)
    
print(s)