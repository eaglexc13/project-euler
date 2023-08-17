# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:54:47 2018

@author: jamicali
"""
from functools import lru_cache

@lru_cache(maxsize=256)
def Fib(x):
    x = int(x)
    if x < 3:
        return 1
    return Fib(x-1) + Fib(x-2)

maxDigits = 0
n = 0
for i in range(200):
    n = Fib(i)
    st = str(n)
    if len(st) > maxDigits:
        print("New max digit length of",len(st),"at i =",i)
        maxDigits = len(st)
#%%

maxDigits = 0
x1 = 1
x2 = 1
x = 0
count = 2
while maxDigits < 1000:
    x = x1 + x2
    x2 = x1
    x1 = x
    maxDigits = len(str(x))
    count += 1
print("Thousand digit Fibonacci number at index",count)