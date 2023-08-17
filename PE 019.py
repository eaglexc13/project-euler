# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:41:50 2018
@PE_019.py
How many Sundays fell on the first of the month 
during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

@author: jamicali

Sunday = 0
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6

"""
months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

start = 1
curDay = 1 #1900-1-1 was a Monday
month = 1 #January is month 1
year = 1900
count = 0

while year < 2001:
    curDay += 1                 #increment the overall day count
    start += 1                  #increment the day-of-month count
    
    #Only update feb days if it LY, Feb, and incorrect
    if (not year % 4) and (month == 2) and (not months[2] == 29) and (not year == 1900):
        months[2] = 29          #Feb has 29 days if leap year
        
    #Only update feb days if not LY, not Feb, and incorrect
    if ((year % 4) or (not month == 2)) and (not months[2] == 28):
        months[2] = 28
        
    if curDay > months[month]:  #if we are at month's end
        curDay = 1              #start next month
        month += 1
        if month > 12:          #if we are at year's end
            month = 1           #start at January
            year += 1           #of next year
            
        #Are we on a Sunday after 1900? (It's already start of month)
        if year > 1900 and not start % 7:       
            count += 1          #Increment the final count
        
print("There were",count,"first-of-month Sundays")