# -*- coding: iso-8859-1 -*-
import urllib
import re
from xml.etree.ElementTree import parse

# Liste der ISBNs, die bei der DNB abgefragt werden
booklist = ['978-3-525-30069-5'] #'978-3-525-30074-9', '978-3-525-30073-2', '978-3-525-30172-2'

DDClist = []
RDFXMLlist = list()

for isbn in booklist:
    urllink = 'https://portal.dnb.de/opac.htm?method=showFullRecord&currentResultId=%22' + isbn + '%22%26any&currentPosition=0'
    url_open = urllib.urlopen(urllink)
    url_data = url_open.read()
    dnbid = re.findall('uri.+3D([0-9]+)', url_data)
    for idvalue in dnbid:
        rdfxmllink = 'http://d-nb.info/' + idvalue + '/about/lds'
        rdfxmlopen = urllib.urlopen(rdfxmllink)
        rdfxml_data = rdfxmlopen.read()
        write_rdfxml_in_file = open('isbn978-3-525-30069-5.xml', 'wb')   # Anlegen einer Datei, in der die Daten gespeichert werden
        write_rdfxml_in_file.write(rdfxml_data)      # Daten in die Datei schreiben
        write_rdfxml_in_file.close()      # Datei schließen

        
        #print url_data
    #break
    #for line in url_data:
    #    line.rstrip()
    #    print line
#    DDC = re.findall('DDC-Notation.*([0-9][0-9][0-9][.][0-9][0-9])', url_data)
#    DDClist.append(DDC)

#print DDClist
#print RDFXMLlist
