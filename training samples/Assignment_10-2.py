# -*- coding: iso-8859-1 -*-

'''10.2 Write a program to read through the mbox-short.txt 
and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
*****
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
*****
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. 
Note that the autograder does not have support for the sorted() function.'''

name = raw_input("Enter file:")
if len(name) < 1 : name = "C:\Users\PeterH\Documents\mbox-short.txt"
handle = open(name)

hours = dict()

for line in handle:
    if not line.startswith('From') or line.startswith('From:'): continue
    else :
        time = line.split()
        time = time[5]
        hour = time.split(':')
        hour = hour[0]
        hours[hour] = hours.get(hour, 0) + 1
        
mail_time = list()

for k, v in hours.items():
    mail_time.append( (k, v) )
    
mail_time.sort()

for k, v in mail_time:
    print k, v