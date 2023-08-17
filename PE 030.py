# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time

def sumFifths(x):
    answer = 0
    for char in str(x):
        answer += int(char)**5
    return answer

def findFifths():
    answer = []
    
    for i in range(2,300000):
        if i == sumFifths(i):
            answer.append(i)
    return answer

start = time.time()
answer = findFifths()
print(answer, sum(answer))
stop = time.time()
print("Complete in",stop-start,"seconds")