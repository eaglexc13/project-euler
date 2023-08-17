# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 14:52:42 2018

@author: jamicali
"""
import time

def wordValue(x):
    ans = 0
    for char in x:
        ans += ord(char) - 64
    return ans

def triangleWords():
    with open('p042_words.txt','r') as words:
        wordList = list(words.readline().split(","))
    
    for index in range(len(wordList)):
        wordList[index] = wordList[index][1:len(wordList[index])-1]
    
    triNums = []
    for n in range(30):
        triNums.append((n * (n + 1))//2)
        
    count = 0
    for word in wordList:
        if wordValue(word) in triNums:
            count += 1
    
    return count

start = time.time()
print(triangleWords())
stop = time.time()
print(stop-start, "seconds elapsed")