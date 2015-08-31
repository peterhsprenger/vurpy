# Open the file mbox-short.txt and read it line by line. 
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line 
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "c:/Users/PeterH/Documents/mbox-short.txt"

fh = open(fname)
mailinglist = list()
count = 0
f = open('c:/Users/PeterH/Documents/mailinglist.txt', 'w')
for line in fh :
    if not line.startswith('From ') : continue
    else: 
        count = count + 1
        item = line.split()
        item = item[1]
        print item
        mailinglist.append(item)
for each in mailinglist : 
    print each
# mit dieser Methode werden die Daten ausserdem in eine Datei ausgegeben
    f.write(each + "; \n")
print "There were", count, "lines in the file with From as the first word"