# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 09:59:06 2018

@author: jamicali
"""
import time
import math
from functools import lru_cache

@lru_cache(maxsize = 5000)
def isPrime(x):
    x = abs(x)
    if x == 1:
        return False
    elif x < 4:
        return True
    elif not x % 2:
        return False
    elif x < 9:
        return True
    elif not x % 3:
        return False
    else:
        r = int(math.sqrt(x))
        f = 5
        while f <= r:
            if not x % f:
                return False
            if not x % (f+2):
                return False
            f += 6
    return True
#%%
answer = []
i = 11

start = time.time()
while len(answer) < 11:
    j = i + 2
    if isPrime(i):
        l_i = int(str(i)[::-1][1:][::-1])
        r_i = int(str(i)[1:])
        while isPrime(l_i) and isPrime(r_i):
            if len(str(l_i)) == 1:
                answer.append(i)
                break
            l_i = int(str(l_i)[::-1][1:][::-1]) #fix case where empty string
            r_i = int(str(r_i)[1:])

    if isPrime(j):
        l_j = int(str(j)[::-1][1:][::-1])
        r_j = int(str(j)[1:])
        while isPrime(l_j) and isPrime(r_j):
            if len(str(l_j)) == 1:
                answer.append(j)
                break
            l_j = int(str(l_j)[::-1][1:][::-1])
            r_j = int(str(r_j)[1:])
            
    i += 6
stop = time.time()
print(answer)
print(sum(answer))
print(stop-start,"seconds elapsed")