# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:04:11 2018

@author: jamicali
"""
# HOW DOES THIS WORK
import math

nums = [0,1,2,3,4,5,6,7,8,9]
limit = 999999 # Don't use 1000000 because you fencepost it
j = 0
mult = [0 for _ in range(10)]
for i in range(9,-1,-1):
    f = math.factorial(i)
    rem = limit // f
    mult[j] = rem
    limit = limit % f
    j += 1
    
for char in range(len(mult)-1,-1,-1):
    for n in range(char+1,len(mult)):
        if mult[char] <= mult[n]:
            mult[n] += 1
    
print(''.join(map(str,mult)))
#%%
