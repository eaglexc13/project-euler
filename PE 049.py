# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:33:06 2018

@author: jamicali
"""

import itertools as it
import math
import time

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

def main():
    start = 1117
    perm = list(it.permutations(str(start)))
    