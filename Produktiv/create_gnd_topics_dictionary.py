import re
import sys

sw = open('C:/Users/PeterH/eclipse/vurpy/X02interimresults/swutf.txt', 'r')
out = 'C:/Users/PeterH/eclipse/vurpy/X03resultdocs/GNDDictionary.txt'

gnddict = dict()

for line in sw:
    id = re.findall('([0-9-X]{5,10})\t', line)
    key = id[0]
    #print id, type(id)
    #print key, type(key)
    topic = re.findall('\t([^.*$]+)', line)
    #print topic, type(topic)
    gnddict[key] = topic

sysout = open(out, 'w')
sysout.write(str(gnddict))

print len(gnddict)

  
    