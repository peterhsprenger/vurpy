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
checkagains = ['9783525255292', '9783525510018', '9783525401361', '9783525630242', '3525614683', '9783647401805', '9783525315279', '9783525370223', '9783647550527', '9783647403236', '9783525350799', '9783647900100', '9783647996363', '9783647569222', '9783647701400', '9783647564005', '9783647770109', '9783647580180', '9783647701264', '9783647512150', '9783647536088', '9783647451879', '9783647462516', '9783525630549', '9783647490625', '9783647581712', '9783647900049', '9783647567105', '9783647536095', '9783525560167', '9783862348817', '9783847101468', '9783899718744', '9783899717044', '9783899711875', '9783899713763', '9783862341108']
isbnprefixes = ['9783525' , '9783647' , '97838252' , '97838385' , '97838470' , '97838471' , '978386234' , '978389971']


def parse_DNBsite_for_sachgruppen_AGAIN(source, mapping):
    out = outputpath + 'checkresults.txt'
    checks = dict()
    for src in source :
        inp = inputpath + 'dictDNB_' + src + 'sg.txt'
        finp = open(inp)        
        dinp = eval(finp.read())
        count = 0
        sachgruppen = []
        for map in mapping :
            try :
                uriline = dinp[map][1][0]
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
                
                checks[map] = sachgruppen
                count = count + 1
                print 'Iteration', count
                print checks        
            
            except :
                continue
    

        
    sysout = open(out, 'w')
    sysout.write(str(checks))


parse_DNBsite_for_sachgruppen_AGAIN(isbnprefixes, checkagains)