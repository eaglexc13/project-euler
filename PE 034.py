# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:37:49 2018

@author: jamicali
"""

import math
import time

max_value = 2540160

def sumFactDigits(x):
    answer = 0
    st_x = str(x)
    for char in st_x:
        answer += math.factorial(int(char))
    return answer
#%%
def main():
    answer = []
    for n in range(3,max_value):
        if n == sumFactDigits(n):
            answer.append(n)
    return answer
#%%
#print(sumFactDigits())
start = time.time()
print(sum(main()))
stop = time.time()
print(stop-start,"seconds elapsed")