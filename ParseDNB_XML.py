# -*- coding: iso-8859-1 -*-

# basierend auf der Einführung in XML: http://www.diveintopython3.net/xml.html

import xml.etree.ElementTree as etree


# rdf_file = 'C:/Users/PeterH/Documents/05 moocs/Programming for Everybody (Python)/1051595762_bibframe.rdf'
rdf_file = 'C:/Users/PeterH/Documents/05 moocs/Programming for Everybody (Python)/1051595762_lds.rdf'

# das XML vollständig parsen
tree = etree.parse(rdf_file)

# das root-Element des XML finden
root = tree.getroot()
print "ROOT-ELEMENT:", root

# die Kindelemente des root-Elements finden und anschließend deren Kindelemente finden
for child in root:
    print "CHILD UNDER ROOT", child
    for grandchild in child:
        print("CHILD:", child, "- GRANDCHILD:", grandchild)
        
