# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:12:36 2018

@author: jamicali
"""
import time

start = time.time()
maxPeriod = 0
maxN = 0
order = 0
exp = 1

for n in range(2,1000):
    exp = n
    order = 0
    if n % 2 and n % 5:
        while not order == 1:
            exp -= 1
            order = 10**exp % n
            if order == 1 and exp > maxPeriod:
                maxPeriod = exp
                maxN = n
stop = time.time()
print("Longest period of",maxPeriod,"at",maxN,"in",stop-start,"seconds")
            
        