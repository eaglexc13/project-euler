#%%
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 09:43:06 2018

@author: jamicali
"""
import time
import math

start = time.time()

limit = 28124
divisors = [[] for _ in range(limit)]
abundant = [False for _ in range(limit)]
abSums = [False for _ in range(limit)]
answer = 0

for i in range(1,limit):
    j = 2
    while (i * j) < limit:
        divisors[i*j].append(i)
#        amicable[i*j] += i
        j += 1
        
print("Loop 1 at",time.time()-start)

for item in range(len(divisors)):
    if sum(divisors[item]) > item:
        abundant[item] = True

print("Loop 2 at",time.time()-start)

length = len(abundant)
for i in range(length):
    if abundant[i]:
        for j in range(i,length):
            if abundant[j]:
                try:
                    abSums[i+j] = True
                except IndexError:
                    continue

print("Loop 3 at",time.time()-start)

for i in range(len(abSums)):
    if not abSums[i]:
        answer += i

stop = time.time()
print(stop-start,"seconds")