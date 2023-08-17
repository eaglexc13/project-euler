# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 11:14:17 2018

@author: jamicali
"""
import time

def pandigital(x, y):
    answer = []
    for a in range(1,x):
        st_a = str(a)
        for b in range(a, y):
            st_b = str(b)
            c = a*b
            st_c = str(c)
            #if len(st_a)+len(st_b)+len(st_c) == 9:
            if ''.join(sorted(st_a+st_b+st_c)) == "123456789":
                if c not in answer:
                    answer.append(c)
    return answer

start = time.time()
out = pandigital(100,10000)
stop = time.time()
print(out,"\n",sum(out))
print(stop-start, "seconds elapsed")