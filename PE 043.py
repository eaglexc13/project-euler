# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 15:24:50 2018

@author: jamicali
"""
import time
import itertools as it

# 2.61 seconds
def subDiv():
    ans = 0
    panList= list(it.permutations('0123456789'))
    
    for tup in panList:
        if int(tup[3]) % 2:
            continue
        elif int(tup[2]+tup[3]+tup[4]) % 3:
            continue
        elif int(tup[3]+tup[4]+tup[5]) % 5:
            continue
        elif int(tup[4]+tup[5]+tup[6]) % 7:
            continue
        elif int(tup[5]+tup[6]+tup[7]) % 11:
            continue
        elif int(tup[6]+tup[7]+tup[8]) % 13:
            continue
        elif int(tup[7]+tup[8]+tup[9]) % 17:
            continue
        ans += int(''.join(tup))
    return ans

start = time.time()
print(subDiv())
stop = time.time()
print(stop-start, "seconds elapsed")