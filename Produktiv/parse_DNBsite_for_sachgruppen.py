# -*- coding: iso-8859-1, utf-8 -*-
#from xml.etree.ElementTree import parse
import re
import urllib2
from urllib2 import Request, URLError, HTTPError, urlopen
from pip._vendor.cachecontrol.controller import URI
import sys

# Dieses Skript ergänzt die Sachgruppen zu einem Titeleintrag (die der dreistelligen DDC-Gruppe entspricht). 
# Der Import einer Sachgruppe ist nicht in einem Downloadfile zu den Titeln der DNB enthalten, sondern nur über einen Aufruf der DNB-Webseite möglich.
# Die Sachgruppe wird anhand der Titel in den vorhandenen Dicitionaries gesucht und dort auch ergänzt. 

inputpath = 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/'
outputpath = 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/'
isbnprefixes = ['9783525' , '9783647' , '97838252' , '97838385' , '97838470' , '97838471' , '978386234' , '978389971']

def parse_DNBsite_for_sachgruppen(source):

    for src in source :
        inp = inputpath + 'dictDNB_' + src + '.txt'
        out = outputpath + 'dictDNB_' + src + 'sg.txt'
        finp = open(inp)        
        dinp = eval(finp.read())
        counter = 0        
        for key, value in dinp.items() :
            print '-' * 100
            print key
            uriline = value[1][0]
            print uriline
            req = Request(uriline)
            try: 
                response = urlopen(req, timeout=20).read()
                sachgruppen = re.findall('Sachgruppe\(n\)</strong>\r\n\t{3}</td>\r\n\t{3}<td .*>\r\n\t{9}\r\n\t{11}([^.*$]+?)\r\n', response)
                print sachgruppen
                value.append(sachgruppen)
            except HTTPError, e:
                sachgruppen = ['The server could not fulfill the request.']
                value.append(sachgruppen)
                print 'Error code: ', e.code
            except URLError, e:
                sachgruppen = ['We failed to reach a server.']
                value.append(sachgruppen)
                print 'Reason: ', e.reason
            except :
                sachgruppen = []
                value.append(sachgruppen)
            counter = counter + 1
            print 'Iteration', counter
        print dinp
        
        sysout = open(out, 'w')
        sysout.write(str(dinp))

parse_DNBsite_for_sachgruppen(isbnprefixes)