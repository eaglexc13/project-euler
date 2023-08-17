# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 08:52:47 2018

@author: jamicali
"""
import time
limit = 1000000
answer = 0

start = time.time()
for i in range(limit):
    st_i = str(i)
    if st_i == st_i[::-1]:
        b_i = bin(i)[2:]
        if b_i == b_i[::-1]:
          answer += i
stop = time.time()
print(answer)
print(stop-start, "seconds elapsed")