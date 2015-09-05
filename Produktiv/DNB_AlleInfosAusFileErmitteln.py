# -*- coding: iso-8859-1, utf-8 -*-
from xml.etree.ElementTree import parse
import re
import urllib2
from urllib2 import Request, URLError, HTTPError, urlopen
from pip._vendor.cachecontrol.controller import URI


# die folgenden Skripte geben zu einer ISBN die DNB-ID, den Link des Titeleintrags in der DNB, die OCLC-Nummer, die Schlagworte der GND 
#(gemeinsame Normdatei), den DDC-Code, den Link zum downloadbaren Inhaltverzeichnis und die Sachgruppen auf Basis eines Datenabzugs 
# der Deutschen Nationalbibliothek aus. Basis dieses Metadatenauszugs ist ein Datenabzug aller Titel aus der DNB.

dnb_metadata = dict()           # in diesem Dictionary werden die ISBNs als Key mit der DNB-ID als Value gespeichert

inputfile = 'F:/VLBGoldFiles/sourcefiles/clean97838470.txt'
outputfile = 'F:/VLBGoldFiles/resultfileswithsachgruppen/isbnlist97838470.txt'

def extract_data_from_dnb_download_files(source):
    fh = open(source)
    isbnlist = []
    for line in fh :
        metadata = list()
        if len(re.findall('<bibo:isbn13>([0-9]+)', line)) == 1:
            isbn = re.findall('<bibo:isbn13>([0-9]+)', line)
        elif len(re.findall('<bibo:gtin14>([0-9]+)', line)) == 1:
            isbn = re.findall('<bibo:gtin14>([0-9]+)', line)
        elif len(re.findall('<bibo:isbn10>([0-9]+)', line)) == 1 :
            isbn = re.findall('<bibo:isbn10>([0-9]+)', line)
        else :
            isbn = re.findall('rdf:Description rdf:about="http://d-nb\.info/([0-9X]+)', line)

        try : 
            dnbid = re.findall('rdf:Description rdf:about="http://d-nb\.info/([0-9X]+)', line)
            metadata.append(dnbid)
        except : 
            dnbid = []
            metadata.append(dnbid)
        try :           
            dnburi = re.findall('rdf:Description rdf:about="(http://d-nb\.info/[0-9X]+)', line)
            metadata.append(dnburi)
        except :
            dnburi = []
            metadata.append(dnburi)
        try : 
            oclc = re.findall('(\(OColc\)[0-9]+)', line)
            metadata.append(oclc)
        except : 
            oclc = []
            metadata.append(oclc)
        try : 
            gnd = re.findall('dcterms:subject rdf:resource="http://d-nb\.info/gnd/([0-9-]+)', line)
            metadata.append(gnd)
        except : 
            gnd = []
            metadata.append(gnd)
        try : 
            ddc = re.findall('dewey\.info/class/([0-9]{3}\.[0-9]+)/', line)
            metadata.append(ddc)
        except : 
            ddc = []
            metadata.append(ddc)
        try : 
            toc = re.findall('tableOfContents rdf:resource="http://d-nb\.info/([0-9X-/]+)', line)
            metadata.append(toc)
        except : 
            toc = []
            metadata.append(toc)
        try : 
            authorid = re.findall('bibo:authorList><rdf:Seq><rdf:li rdf:resource="http://d-nb\.info/gnd/([0-9X/]+)', line)
            metadata.append(authorid)
        except : 
            authorid = []
            metadata.append(authorid)
        
        if len(isbn) == 0: pass
        else: dnb_metadata[isbn[0]] = metadata

    print dnb_metadata
       

def parse_DNBsite_for_sachgruppen(source):
    fh = open(source)
    counter = 0
    for line in fh :
        print '-' * 70
        if len(re.findall('<bibo:isbn13>([0-9]+)', line)) == 1 :
            isbn = re.findall('<bibo:isbn13>([0-9]+)', line)
            print 'ISBN13', isbn
        elif len(re.findall('<bibo:gtin14>([0-9]+)', line)) == 1 :
            isbn = re.findall('<bibo:gtin14>([0-9]+)', line)
            print 'GTIN14', isbn
        elif len(re.findall('<bibo:isbn10>([0-9]+)', line)) == 1 :
            isbn = re.findall('<bibo:isbn10>([0-9]+)', line)
            print 'ISBN10', isbn
        else:
            isbn = re.findall('rdf:Description rdf:about="http://d-nb\.info/([0-9X]+)', line)
            print 'DNBID', isbn, '\n\n'

        uriline = re.findall('rdf:Description rdf:about="http://d-nb.info/([0-9X]+)', line)[0]
        print uriline
        urlline = 'http://d-nb.info/' + uriline
#        urlline = 'https://portal.dnb.de/opac.htm?method=simpleSearch&cqlMode=true&query=idn%3DD' + uriline
        req = Request(urlline)
        try: 
            response = urlopen(req).read()
            #site = urllib2.urlopen(urlline).read()
            #print response
            sachgruppen = re.findall('Sachgruppe\(n\)</strong>\r\n\t{3}</td>\r\n\t{3}<td .*>\r\n\t{9}\r\n\t{11}([^.*$]+?)\r\n', response)
            print sachgruppen
            dnb_metadata[isbn[0]].append(sachgruppen)
        except HTTPError, e:
            sachgruppen = ['The server couldn\'t fulfill the request.']
            dnb_metadata[isbn[0]].append(sachgruppen)
            #print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
        except URLError, e:
            sachgruppen = ['We failed to reach a server.']
            dnb_metadata[isbn[0]].append(sachgruppen)
            #print 'We failed to reach a server.'
            print 'Reason: ', e.reason            
        counter = counter + 1
        print 'Iteration', counter
    print dnb_metadata
    

def print_and_save_dictionary_items(dictionary):
    results = open(outputfile, 'w')
    count = 0
    for k, v in dnb_metadata.items(): 
        try:
            count += 1
            print '-'*70
            print 'EINTRAG NR. ' + str(count)
            print 'isbn: ', k, 'Typ k', type(k)
            print '0 - dnbid: ', v[0]
            print '1 - dnburi: ', v[1]
            print '2 - oclc: ', v[2]
            print '3 - gnd: ', v[3]
            print '4 - ddc: ', v[4]
            print '5 - toc: ', v[5]
            print '6 - authorid: ', v[6]
            print '7 - sachgruppen: ', v[7]
            print 
            
            # mit dieser Methode werden die Daten in eine für Escel lesbare CSV Datei ausgegeben
            datatowrite = k + '|' + str(v[0]) + '|' + str(v[1]) + '|' + str(v[2]) + '|' + str(v[3]) + '|' + str(v[4]) + '|' + str(v[5]) + '|' + str(v[6]) + '|' + str(v[7]) + '\n'
            results.write(datatowrite)
        except:
            pass
    
    results.write(str(count) + " Einträge")
    print "Das Dictionary hat", len(dnb_metadata), "Einträge" 



extract_data_from_dnb_download_files(inputfile)
parse_DNBsite_for_sachgruppen(inputfile)
print_and_save_dictionary_items(dnb_metadata)
