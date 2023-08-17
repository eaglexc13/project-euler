# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 12:05:50 2018

@author: jamicali
"""
import time
import math
import itertools

def pentaNumsUpTo(x):
    return [(n * (3* n - 1)) // 2 for n in range(1, x+1)]

def pentaNumsDiff(n):
    return [[(6 * k * n - 3 * k ** 2 - k) // 2 for k in range(1,n)] for n in range(1,n+1)]

def getPentaNum(n):
    return (n * (3 * n - 1)) // 2

def isPentagonal(n):
    pen = (math.sqrt(24 * n + 1) + 1) / 6
    return pen == int(pen)

def findPentaSums():
    ls = pentaNumsUpTo(100)
    pairs = []
    for ind in range(len(ls)):
        p = ls[ind]
        for ind2 in range(ind):
            q = ls[ind2]
            if (p + q) in ls:
                pairs.append([p,q,p+q])
    return pairs

def findPentaDiffs():
    ls = pentaNumsUpTo(100)
    pairs = []
    for ind in range(len(ls)):
        p = ls[ind]
        for ind2 in range(ind):
            q = ls[ind2]
            if abs(p - q) in ls:
                pairs.append([p,q,p-q])
    return pairs

def pentaIndex(x):
    m = (math.sqrt(24 * x + 1) + 1) / 6
    if not m % 1:
        return int(m)
    else:
        return -1

def bruteForce():
    ls = pentaNumsUpTo(1000)
    mini = max(ls)
    
    for ind in range(1, len(ls)):
        p = ls[ind]
        for ind2 in range(1, ind):
            q = ls[ind2]
            if isPentagonal(p + q):
                dif2 = abs(p - q)
                if isPentagonal(dif2):
                    if dif2 < mini:
                        mini = dif2
    return mini

def whileLoop():
    #smallest = False
    found = False
    i = 1
    ans = getPentaNum(10000)
    
    while not found:
        i += 1
        p = getPentaNum(i)
        minDiff= p - getPentaNum(i-1)
        for j in range(i-1,1,-1):
            q = getPentaNum(j)
            if q < minDiff:
                break
            if isPentagonal(p + q):
                dif2 = abs(p - q)
                if isPentagonal(dif2):
                    if dif2 < ans:
                        ans = dif2
                        found = True
    return ans

def stolenCode():
    p = {int((num * ((3 * num )- 1)) / 2) for num in range(1, 3000)}
    
    for x, y in itertools.combinations(p, 2):
        diff = abs(x - y)
        _sum = x + y
        if diff in p and _sum in p:
            print(diff, _sum, x, y)
    
start = time.time()
print(stolenCode())
stop = time.time()
print(stop-start,"seconds elapsed")