# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 19:31:15 2018

@author: jamicali
"""
import time

start = time.time()
count_max = 9999
concat_min = 918273645

max_ans = concat_min
for m in range(1,count_max + 1):
    st = ''
    n = 1
    while len(st) < 9:
        st = st + str(m*n)
        n += 1
    if len(st) == 9 and ''.join(sorted(st)) == "123456789":
        if int(st) > max_ans:
            max_ans = int(st)
    
stop = time.time()
print(max_ans)
print(stop-start,"seconds elapsed")