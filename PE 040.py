# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 08:46:24 2018

@author: jamicali
"""

s = ''

for x in range(1,1000001):
    s += str(x)

#%%
ans = 1
for e in range(7):
    ans = ans * int(s[10**e - 1])

#%%
len(s)