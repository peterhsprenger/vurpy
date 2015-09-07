# -*- coding: utf-8 -*-
import sys
#from check_outputs import isbnprefixes

inputpath = 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/'
isbnprefixes = ['9783525', '9783647', '97838252', '97838385', '97838470', '97838471', '978386234', '978389971']
swdictionary = 'C:/Users/PeterH/eclipse/vurpy/X03resultdocs/GNDDictionary.txt'
outputpath = 'C:/Users/PeterH/eclipse/vurpy/X03resultdocs/'


def collect_all_titles_in_one_list(source):

    swopen = open(swdictionary)
    sweval = eval(swopen.read())
    exceptions = []

    for src in source:

        fsrc = open(inputpath + 'dictDNB_' + src + 'sg.txt')
        dsrc = eval(fsrc.read())

        for dkey, dvalue in dsrc.items() :
            gndtopicnames = []
            for item in dvalue[3]:    
                try : 
                    gndtopicnames.append(sweval[item][0])
                except : 
                    exceptions.append(item)
            dvalue.append(gndtopicnames)
        
        sysout = open(outputpath + 'dictDNB_' + src + 'complete.txt', 'w')
        sysout.write(str(dsrc))        

    print exceptions
    sysout = open('C:/Users/PeterH/eclipse/vurpy/X02interimresults/exceptions.txt', 'w')
    sysout.write(str(exceptions))


collect_all_titles_in_one_list(isbnprefixes)