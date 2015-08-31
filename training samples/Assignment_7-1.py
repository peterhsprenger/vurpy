# Write a program that prompts for a file name, then opens that file and reads through the file, 
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.pythonlearn.com/code/words.txt
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "c:/Users/PeterH/Documents/mbox-short.txt"
fh = open(fname)
ft = fh.read()
fts = ft.strip()
fu = fts.upper()
print fu