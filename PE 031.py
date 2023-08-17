# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:56:02 2018

@author: jamicali
"""
import time
from functools import lru_cache

C = [1, 2, 5, 10, 20, 50, 100, 200]

@lru_cache(maxsize = 256)
def coinCounter(n, k):
    if n < 0 or k < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return coinCounter(n, k-1) + coinCounter(n - C[k], k)
    
start = time.time()
print(coinCounter(200, len(C) - 1), "combinations")
stop = time.time()
print(stop-start,"seconds elapsed")