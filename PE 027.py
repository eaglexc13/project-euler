# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:28:24 2018

@author: jamicali
"""
import math, time
from functools import lru_cache

start = time.time()
@lru_cache(maxsize = 4096)
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

# b must be prime so gen list of primes
b_List = [i for i in range(-999,1000) if isPrime(i)]

# init outputs
longest = 0
answer = 0
ans_a = 0
ans_b = 0

# iterate through list of b
for b in b_List:
    
    #iterate through possible a
    for a in range(-999,1000,2):
        
        n = 1
        # when n = 1, 1 + a + b must be prime
        if isPrime(1 + a + b):
            # Code to find the longest string of consecutive primes
            # Loop until no longer prime
            while isPrime(n**2 + n*a + b):
                n += 1
            # Check if consecutive and update outputs
            if n > longest:
                longest = n
                ans_a = a
                ans_b = b
                answer = a * b

stop = time.time()
print("Longest chain of length:",longest,"\nProduct is:",answer,"\nTime elapsed:",stop-start,"seconds")
            
            