# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:06:04 2018

@author: jamicali
"""

import math
import time

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

# %% 
# Not working! :(
def distinctCalc():
    answer = 0
    
    for x in range(2,101):
        uniques = 99
        if isPrime(x):
            answer += uniques
        else:
            x_list = [x**z for z in range(2,101)]
            for a in range(2,x):
                y = math.log(x,a)
                if (y % 1) == 0:
                    a_list = [a**z for z in range(2,101)]
                    x_list = list(set(x_list) - set(a_list))
            answer += len(x_list)
    return answer
#%%
def bruteForceDistincts():
    answer = []
    for a in range(2,101):
        for b in range(2,101):
            c = a**b
            if not (c in answer):
                answer.append(c)
    return len(answer)
#%%
start = time.time()
print("Brute Force:",bruteForceDistincts())
mid = time.time()
print("Log Calc:",distinctCalc())
stop = time.time()
print("Brute Force:",mid-start)
print("Log Calc:",stop-mid)