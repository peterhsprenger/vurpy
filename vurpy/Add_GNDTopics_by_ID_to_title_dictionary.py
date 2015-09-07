# -*- coding: utf-8 -*-
import sys

inputfiles = ['C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB_9783525sg.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB_9783647sg.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB_97838252sg.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB_97838385sg.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB_97838470sg.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB_97838471sg.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB_978386234sg.txt', 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB_978389971sg.txt']
swdictionary = 'C:/Users/PeterH/eclipse/vurpy/X03resultdocs/GNDDictionary.txt'
out = 'C:/Users/PeterH/eclipse/vurpy/X03resultdocs/completetitlelist.txt'

#dictionary = 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/test.txt'
#swdictionary = 'C:/Users/PeterH/eclipse/vurpy/X03resultdocs/swtest.txt'



def collect_all_titles_in_one_list(source):

    swopen = open(swdictionary)
    sweval = eval(swopen.read())

    for src in source:
        fsrc = open(src)
        dsrc = eval(fsrc.read())

        for dkey, dvalue in dsrc.items() :
            gndtopicnames = []
            for item in dvalue[3]:
                gndtopicnames.append(sweval[item][0])
                print gndtopicnames
            dvalue.append(gndtopicnames)
        print dsrc
        
#    sysout = open(out, 'w')
#    sysout.write(str(gnddict))    

collect_all_titles_in_one_list(inputfiles)