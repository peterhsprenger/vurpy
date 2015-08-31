# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() function. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.
fname = raw_input("Enter file name: ")
if len(fname) == 0 :
    fname = 'C:/Users/PeterH/Documents/romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    fhsplit = line.split()
    for item in fhsplit :
         if item in lst : continue
         else : 
             lst.append(item)
lst.sort()
print lst