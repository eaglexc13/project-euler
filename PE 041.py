# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 15:48:59 2018

@author: jamicali
"""
import math
import time
from functools import lru_cache
import itertools as it

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

@lru_cache(maxsize = 128)
def pandigit(x):
    ans = ''
    for i in range(x):
        ans += str(i + 1)
    return ans

def isPandigital(x):
    return pandigit(len(str(x))) == ''.join(sorted(str(x)))

# Takes about 1500 seconds to run
# Not efficient
# BUT the largest pandigital prime is < 9876543 (runtime ~ 1 second)
# BUT you don't know that until you guess the answer
# HOW do you make this better??
def brutePandigitPrime():
    ans = 2143
    n = 7652413
    while n <= 987654321:
        if isPandigital(n):
            if isPrime(n):
                ans = n
        if isPandigital(n + 4):
            if isPrime(n + 4):
                ans = n + 4
        n += 6
    return ans

# Itertools has a permutations method!!!
# Runs in .373 seconds checking all the way to 987654321
# BUT any permutation of length 8 or 9 will be divisible by 3 
# Just add them up -> sum(range(9)) == 36 and sum(range(10)) == 45
def betterPandigitPrime():
    ans = 2143
    pandigital = '123456789'
    for n in range(4,10):
        panList = list(it.permutations(pandigital[:n]))
        for tup in panList:
            num = int(''.join(tup))
            if isPrime(num):
                if num > ans:
                    ans = num
    return ans

start = time.time()
print(betterPandigitPrime())
stop = time.time()
print(stop-start,"seconds elapsed")
