# -*- coding: utf-8 -*-
import sys
import re
import urllib2
from urllib2 import Request, URLError, HTTPError, urlopen
from pip._vendor.cachecontrol.controller import URI

sourcefiles = ['C:/Users/PeterH/eclipse/vurpy/X02interimresults/dict9783525.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dict9783647.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dict97838252.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dict97838385.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dict97838470.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dict97838471.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dict978386234.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dict978389971.txt']
mappingfile = ['C:/Users/PeterH/eclipse/vurpy/X01inputdocs/Schlagworte_utf8dict.txt']
resultfiles = ['C:/Users/PeterH/eclipse/vurpy/X03resultdocs/final9783525.txt', 'C:/Users/PeterH/eclipse/vurpy/X03resultdocs/final9783647.txt', 'C:/Users/PeterH/eclipse/vurpy/X03resultdocs/final97838252.txt', 'C:/Users/PeterH/eclipse/vurpy/X03resultdocs/final97838385.txt', 'C:/Users/PeterH/eclipse/vurpy/X03resultdocs/final97838470.txt', 'C:/Users/PeterH/eclipse/vurpy/X03resultdocs/final97838471.txt', 'C:/Users/PeterH/eclipse/vurpy/X03resultdocs/final978386234.txt', 'C:/Users/PeterH/eclipse/vurpy/X03resultdocs/final978389971.txt']

def add_GNDTopic_from_metadata_file(input, mapping, output):
    #fc = open(compares)
    #comparedict = eval(fc.read())
    #print mappingdict
    #print type(mappingdict)
    #sys.stdout.write(comparedict)

    fmap = open(mapping[0])
    print fmap
    dmap = eval(fmap.read())
    print dmap
    '''        
    for inp in input :
        finp = open(inp)
        inp_dict = eval(finp.read())

        for isbn in inp_dict.keys() :
            gndtopic = []
            #print isbn
            for gndid in inp_dict[isbn][3] :
                #print gndid
                try : 
                    gndtopic.append(map_dict[gndid])
                except : 
                    continue
            inp_dict[isbn].append(gndtopic)
        print inp_dict
        result = str(inp_dict)
        for out in output :
            sysout = open(out, 'w')
            sysout.write(result)
            
    '''    
add_GNDTopic_from_metadata_file(sourcefiles, mappingfile, resultfiles)
