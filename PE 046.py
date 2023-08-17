# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 10:32:24 2018

@author: jamicali
"""
import time
import math
import numpy as np
#%%
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
#%%
def twiceSquareList(n):
    return [2*i**2 for i in range(1,n)]
#%%
def primesFrom2To(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(int(n//3 + (n%6==2)), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)//3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]
#%%
def nextPrime(n):
    if not n % 2:
        m = n + 1
    else:
        m = n + 2
    while not isPrime(m):
        m = m + 2
    return m
#%%
def main():
    square = 6
    num = 35
    square_list = [1,4,9,16,25,36]
    prime_list = list(primesFrom2To(1000000))
    found = False
    
    while not found:
        num = num + 2
        while num > max(prime_list):
            prime_list.append(nextPrime(max(prime_list)))
        while num > max(square_list):
            square = square + 1
            square_list.append(square ** 2)
        if num not in prime_list:
            