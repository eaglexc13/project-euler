# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:59:29 2018

@author: jamicali
"""
import math
import time

def isPentagonal(n):
    pen = (math.sqrt(24 * n + 1) + 1) / 6
    return pen == int(pen)

def isTriangular(n):
    tri = (math.sqrt(8 * n + 1) - 1) / 2
    return tri == int(tri)

# 1533776805
# 0.020554304122924805 seconds elapsed
def main():
     i = 143
     #found = False
     
     while True:#not found:
         i += 1
         q = i * (2 * i - 1)
         if isPentagonal(q) and isTriangular(q):
             return q
         
start = time.time()
print(main())
stop = time.time()
print(stop-start,"seconds elapsed")