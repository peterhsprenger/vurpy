# -*- coding: iso-8859-1, utf-8 -*-
import re
import sys

inputpath = 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/'
mappingpath = 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/'
outputpath = 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/'
isbnprefixes = ['9783525' , '9783647' , '97838252' , '97838385' , '97838470' , '97838471' , '978386234' , '978389971']

def check_outputfiles(isbn) :
    for isb in isbn : 
        inp = inputpath + 'dictDNB_' + str(isb) + '.txt'
        map = mappingpath + 'dictDNB_' + str(isb) + 'sg.txt'
        out = outputpath + 'dictDNB_' + str(isb) + 'checkagain.txt'
            
        finp = open(inp)
        fmap = open(map)
        dinp = eval(finp.read())
        dmap = eval(fmap.read())
        
        maplist = list()
        checkagain = list()
        
        for kmap, vmap in dmap.items() :
            maplist.append(kmap)
            if len(vmap) < 8 or str(vmap[7]) == 'The server could not fulfill the request.' or str(vmap[7]) == 'We failed to reach a server.' :
                checkagain.append(kmap)
            else : 
                continue
                
        for kinp, vinp in dinp.items() :
            if kinp in maplist :
                continue
            else :
                checkagain.append(kinp)                 

        if len(checkagain) > 0 : 
            sysout = open(out, 'w')
            sysout.write(str(checkagain))
        else :
            continue
         
check_outputfiles(isbnprefixes)