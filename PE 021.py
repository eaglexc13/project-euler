# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:45:09 2018

@author: jamicali
"""

# Create list of lists of proper divisors
# 1 has no proper divisors
# Primes have proper divisors of [1]
# All numbers have 1 as a proper divisor
# Only have to check the first 100 numbers (100*100=10 000)
# For i in range(2,101):
#     j = 1 # iterate through all multiples of i
#     while i*j < 10000:
#         
# Create list of sums of proper divisors
import time

start = time.time()
divisors = [[] for _ in range(10000)]
amicable = [1 for _ in range(10000)]

for i in range(2,10000):
    j = 2
    while (i * j) < 10000:
        divisors[i*j].append(i)
        amicable[i*j] += i
        j += 1
        
answer = 0
ls = []
for i in range(2,len(amicable)):
    try: 
        if amicable[amicable[i]] == i and (not amicable[i] == i):
            ls.append(i)
            answer += i
    except IndexError:
        continue

stop = time.time()
print("Amicable numbers under 10000 sum to",answer,"in",stop-start,"seconds")