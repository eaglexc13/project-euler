# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 07:26:29 2018

@author: jamicali
"""
import time

start = time.time()
# List for name manipulation
nameList = []

# Comma separated names split into a list
with open('p022_names.txt', 'r') as names:
    nameList = list(names.readline().split(","))
    
# Trim the quotation marks
for n in range(len(nameList)):
    nameList[n] = nameList[n][1:(len(nameList[n])-1)]
    
# Sort alphabetically
nameList.sort()
# Init answer
answer = 0
# Testing
#for char in nameList[937]:
#    print(char,ord(char)-64)

# Find sum of each name, multiply by position, add to final sum
for index in range(len(nameList)):
    temp = 0
    for char in nameList[index]:
        temp += ord(char)-64
    answer += (index + 1) * temp

stop = time.time()
print(answer,"found in",stop-start,"seconds")

    
    
