# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:35:50 2018

@author: jamicali
"""
import time
import math

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
def rotations(x):
    answer = [x]
    temp = str(x)[1:] + str(x)[:1]
    while not temp == str(x):
        answer.append(int(temp))
        temp = temp[1:] + temp[:1]
    return answer
#%%
def circularPrime(x):
    for rot in rotations(x):
        if isPrime(rot):
            continue
        else:
            return False
    return True
    
#%%

#print(rotations(443123))
#print(circularPrime(197))
def main():
    count = 13
    limit = 1000000
    i = 101
    while i < limit:
        if circularPrime(i):
            count += 1
        if circularPrime(i+2):
            count += 1
        i += 6
    return count

start = time.time()
print(main())
stop = time.time()
print(stop-start,"seconds elapsed")
        