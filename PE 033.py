# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 16:21:49 2018

@author: jamicali
"""

def digitCancel():
    answer = []
    for a in range(1,10):
        for b in range(a,10):
            for c in range(1,10):
                num = int(str(a)+str(b))
                den = int(str(b)+str(c))
                if (num/den) == (a/c) and not(a == b):
                    answer.append(str(num)+"/"+str(den))
    return answer
#%%
def main():
    ans = digitCancel()
    num = 1
    den = 1
    for item in ans:
        num *= int(item[:2])
        den *= int(item[3:])
    return str(num)+"/"+str(den)
#%%
import time
start = time.time()
print(main())
stop = time.time()
print(stop-start,"seconds elapsed")