# -*- coding: iso-8859-1, utf-8 -*-
from xml.etree.ElementTree import parse
import re
import urllib2
from urllib2 import Request, URLError, HTTPError, urlopen
from pip._vendor.cachecontrol.controller import URI

dnb_metadata = dict()           # das Dictionary, dessen Inhalt als CSV gedruckt werden soll

inputfiles = 'F:/VLBGoldFiles/sourcefiles/clean97838470.txt'
outputfiles = 'F:/VLBGoldFiles/resultfileswithsachgruppen/isbnlist97838470.txt'


def print_and_save_dictionary_items(dictionary):
    results = open(outputfile, 'w')
    count = 0
    
    fmap = open(mapping[0])
    map_dict = eval(fmap.read())
    
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


print_and_save_dictionary_items(dnb_metadata)
