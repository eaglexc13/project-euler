# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:27:14 2018

@author: jamicali
"""
import time

def squareList(list):
    return [x**2 for x in list]

def sideLengths():
    p = {x:0 for x in range(1,1001)}
    
    for a in range(1,334):
        for b in range(a,1000-a):
            for c in range(b+1,1000-a-b):
                if a**2 + b**2 == c**2:
                    p[a+b+c] += 1
    return max(p, key=lambda key: p[key])

start = time.time()
print(sideLengths())
stop =time.time()
print(stop-start,"seconds elapsed")