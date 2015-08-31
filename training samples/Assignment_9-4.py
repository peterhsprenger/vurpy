# -*- coding: iso-8859-1 -*-

'''9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''

name = raw_input("Enter file:")
# mit der folgenden if-Bedingung wird ein Filename automatisch übernommen, wenn die Eingabe des Users durch raw_input eine Länge von 0 Zeichen hat
if len(name) == 0:
    name = "C:\Users\PeterH\Documents\mbox-short.txt"
# if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mails = dict()

# in dieser Schleife wird eine Liste aller Absender erzeugt, indem aus der mit "From:" beginnenden Zeile jeweils das zweite Word einer Liste
# hinzugefügt wird. Dies sind die Absender. Dieses zweite Wort wird dann an das Dictionary als key übergeben. Dabei wird automatisch mit jedem
# neuen Auftreten eines Absenders dieser dem Dictionary entweder hinzugefügt oder die Häufigkeit des Auftauchens im Zähler (value) des key summiert
for line in handle:
    if not line.startswith('From ') : continue
    else :
        sent_from = line.split()
        sent_from = sent_from[1]
        mails[sent_from] = mails.get(sent_from, 0) + 1
        print mails
        break

# Es werden zwei Variablen erzeugt für das den am häufigsten auftretenden Absender und die Häufigkeit seines Auftauchens
max_sender = None
max_sent = None

# Mit dieser Schleife wird ermittelt welcher Absender im Dictionary am häufigsten auftaucht. 
# sender und count sind Variablen für das key-value-pair des dictionaries; wenn der count eines dictionary-Eintrags gräßer ist
# als der bisher in der Schleife ermittelte count eines anderes Absendersm wird dieser der Variable max_sender zugewiesen. 
for sender,count in mails.items():
#    if count is None or count > max_sent:
    if count > max_sent:
        max_sender = sender
        max_sent = count
print max_sender, max_sent