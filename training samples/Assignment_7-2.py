# -*- coding: iso-8859-1 -*-

# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines 
# and compute the average of those values and produce an output as shown below.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.
# C:\Users\PeterH\Documents\mbox-short.txt
fname = raw_input("Enter file name: ")
# mit der folgenden if-Bedingung wird ein Filename automatisch übernommen, wenn die Eingabe des Users durch raw_input eine Länge von 0 Zeichen hat
if len(fname) == 0:
    fname = "C:\Users\PeterH\Documents\mbox-short.txt"
fh = open(fname)
confidence = 0
linecounter = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else : 
        linecounter = linecounter + 1
        startpos = line.rfind(' ')
        number = line[startpos+1:]
        confidence = confidence + float(number)
print "Average spam confidence:", confidence / linecounter