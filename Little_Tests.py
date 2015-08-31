# -*- coding: iso-8859-1 -*-
# -*- coding: ascii -*-
# -*- coding: utf8 -*-

import xml.etree.ElementTree as etree
import urllib
import re
from pydoc import Doc
from xml.etree.ElementTree import parse
from xml.dom.minidom import parse
import rdflib
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF
import BeautifulSoup


#rdf_file = 'C:/Users/PeterH/Documents/05 moocs/Programming for Everybody (Python)/1051595762_lds.rdf'
rdf_file = 'http://experiment.worldcat.org/oclc/63108987.rdf' #846557519.rdf'
dnb_rdf = 'http://d-nb.info/1052140025/about/lds'
xml_file = 'C:/Users/PeterH/AppData/Local/Temp/1051401852_marcxml.xml'

g = rdflib.Graph()
result = g.parse(rdf_file)

print("graph has %s statements." % len(g))
# prints graph has 79 statements.


# Iterate over triples in store and print them out.
print("--- printing raw triples ---")
for s, p, o in g:
    #if str(p) == 'http://schema.org/about' :    #str(s).startswith('http://id.worldcat.org/fast/') and 
    print 'SUBJECT', s, type(s)
    print 'STRING SUBJECT', str(s)
    print 'PREDICAT', p
    print 'OBJECT', o
    print '\n'


oclc_url = urllib.urlopen('http://www.worldcat.org/oclc/846557519').read()
soup = BeautifulSoup('http://www.worldcat.org/oclc/846557519')
    #<li class="subject-term">
    #<a href="/search?q=su%3AProtestantismus.&qt=hot_subject" lang='' title="Suche nach weiteren Themengebieten">Protestantismus.</a>

soup.find_all('a')




# For each foaf:Person in the store print out its mbox property.
#print("--- printing mboxes ---")
#for description in g.subjects(RDF.type RDF.resource):
 #   for topic in g.objects(person, FOAF.mbox):
 #       print(mbox)




#das XML vollstandig parsen
#tree = etree.parse(rdf_file)
#tree2 = etree.fromstring(xml_file)
#print 'OCLC-ID: ', tree2.find('datafield').text

#isbn = '9783525100264'
#dnb_url = 'https://portal.dnb.de/opac.htm?method=showFullRecord&currentResultId=%22' + isbn + '%22%26any&currentPosition=0'
