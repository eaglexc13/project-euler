# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:58:15 2018

@author: jamicali
"""

tri = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

gridTri = [line.split(" ") for line in tri.split("\n")]
for i in range(len(gridTri)):
    gridTri[i] = list(map(int,gridTri[i]))

bot = []
temp = []

#assign copy of gridTri[lastrow] to bot
bot = list(gridTri[len(gridTri)-1])

for row in range(len(gridTri)-2,-1,-1): #iterate rows from [2nd to last] up to first
    for item in range(len(gridTri[row])): #iterate items in each row
        #append (current row items + max of bot items) to temp
        temp.append(gridTri[row][item] + max(bot[item], bot[item+1])) #gridTri[row][item]
    print(gridTri[row+1],"\n",temp)
    #make temp the new bot (now with added values)
    bot = list(temp)
    #reset temp
    temp = []
print(bot)