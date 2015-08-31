# -*- coding: iso-8859-1 -*-
from xml.etree.ElementTree import parse
import re
import urllib


# die folgenden Skripte geben die ISBN; DNB-ID und den Link des Titels zur ID auf Basis eines Datenabzugs der Deutschen Nationalbibliothek aus

dnb_id4isbn = dict()       # in diesem Dictionary werden die ISBNs als Key mit der DNB-ID als Value gespeichert
dnb_uri4isbn = dict()      # in diesem Dictionary werden die ISBNs als Key mit dem URI zum Volleintrag gespeichert
dnb_isbnlist = list()        # in dieser Liste werden nur die DNB-IDs gespeichert 

fname = 'F:/VLBGoldFiles/sourcefiles/shorttest9783525.txt'


def extract_ids_from_dnb_download(source):
    fh = open(fname)
    for line in fh :
        try:
            isbn = re.findall('<bibo:isbn13>([0-9]+)', line)
            iduri = list()
            dnbid = re.findall('rdf:Description rdf:about="http://d-nb.info/([0-9X]+)', line)
            iduri.append(dnbid)
            dnburi = re.findall('rdf:Description rdf:about="(http://d-nb.info/[0-9X]+)', line)
            iduri.append(dnburi)
            dnb_id4isbn[isbn[0]] = iduri        
        except:
            continue
    
    print dnb_id4isbn
    print "Das Dictionary hat", len(dnb_id4isbn), "Einträge" 
    
def print_and_save_dictionary_items(dictionary):
    results = open('F:/VLBGoldFiles/resultfiles/isbnlist9783525.txt', 'w')
    count = 0
    for k, v in dnb_id4isbn.items(): 
        count += 1
        if len(v[0]) == 10 :
            print "EINTRAG " + str(count) + ":    ISBN ", k, "  |  ID ", v[0], "  |  URI ", v[1]
        else:    
            print "EINTRAG " + str(count) + ":    ISBN ", k, "  |  ID ", v[0], "   |  URI ", v[1]
        # mit dieser Methode werden die Daten ausserdem in eine Datei ausgegeben
        results.write(k + '|' + v[0] + '|' + v[1] + "\n")
    results.write(str(count) + " Einträge")

extract_ids_from_dnb_download(fname)
print_and_save_dictionary_items(dnb_id4isbn)