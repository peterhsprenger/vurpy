# -*- coding: iso-8859-1, utf-8 -*-
import re
import sys


# Das Skript analysiert die Download-Dateien der DNB und schreibt für jede ISBN die dazugehörige DNB-ID, den Link des Titeleintrags in der DNB, 
# die OCLC-Nummer, die ID der GND (gemeinsame Normdatei), den DDC-Code, den Link zum downloadbaren Inhaltverzeichnis und die Sachgruppen als
# Python-Dictionary in eine Textdatei.


inputpath = 'C:/Users/PeterH/eclipse/vurpy/X01inputdocs/'
outputpath = 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/'
isbnprefixes = ['9783525' , '9783647' , '97838252' , '97838385' , '97838470' , '97838471' , '978386234' , '978389971']

#inputfiles = ['C:/Users/PeterH/eclipse/vurpy/X01inputdocs/clean9783525.txt' , 'C:/Users/PeterH/eclipse/vurpy/X01inputdocs/clean9783647.txt' , 'C:/Users/PeterH/eclipse/vurpy/X01inputdocs/clean97838252.txt' , 'C:/Users/PeterH/eclipse/vurpy/X01inputdocs/clean97838385.txt' , 'C:/Users/PeterH/eclipse/vurpy/X01inputdocs/clean97838470.txt' , 'C:/Users/PeterH/eclipse/vurpy/X01inputdocs/clean97838471.txt' , 'C:/Users/PeterH/eclipse/vurpy/X01inputdocs/clean978386234.txt' , 'C:/Users/PeterH/eclipse/vurpy/X01inputdocs/clean978389971.txt']
#outputfiles = ['C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB9783525.txt' , 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB9783647.txt' , 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB97838252.txt' , 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB97838385.txt' , 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB97838470.txt' , 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB97838471.txt' , 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB978386234.txt' , 'C:/Users/PeterH/eclipse/vurpy/X02interimresults/dictDNB978389971.txt']


def extract_data_from_dnb_download_files(isbnprefixes):

    for isbn in isbnprefixes :
        inp = inputpath + 'clean' + isbn + '.txt'
        out = outputpath + 'dictDNB_' + isbn + '.txt'
        
        finp = open(inp)
        dnb_metadata = dict()
        for line in finp :
            metadata = list()
            if len(re.findall('<bibo:isbn13>([0-9]{13})', line)) == 1:
                isbn = re.findall('<bibo:isbn13>([0-9]{13})', line)
            elif len(re.findall('<bibo:gtin14>([0-9]{13})', line)) == 1:
                isbn = re.findall('<bibo:gtin14>([0-9]{13})', line)
            elif len(re.findall('<bibo:isbn10>([0-9X]{10})', line)) == 1 :
                isbn = re.findall('<bibo:isbn10>([0-9X]{10})', line)
            else :
                isbn = re.findall('rdf:Description rdf:about="http://d-nb\.info/([0-9X-]+)', line)

            dnbid = re.findall('rdf:Description rdf:about="http://d-nb\.info/([0-9X]+)', line)
            metadata.append(dnbid)

            dnburi = re.findall('rdf:Description rdf:about="(http://d-nb\.info/[0-9X]+)', line)
            metadata.append(dnburi)

            oclc = re.findall('(\(OColc\)[0-9]+)', line)
            metadata.append(oclc)

            gnd = re.findall('dcterms:subject rdf:resource="http://d-nb\.info/gnd/([0-9-]+)', line)
            metadata.append(gnd)

            ddc = re.findall('dewey\.info/class/([0-9]{3}\.[0-9]+)/', line)
            metadata.append(ddc)

            toc = re.findall('tableOfContents rdf:resource="http://d-nb\.info/([0-9X\-\/]+)', line)
            metadata.append(toc)

            authorid = re.findall('bibo:authorList><rdf:Seq><rdf:li rdf:resource="http://d-nb\.info/gnd/([0-9X/]+)', line)
            metadata.append(authorid)

            if len(isbn) == 0: continue
            else: dnb_metadata[isbn[0]] = metadata
    
        print inp 
        print len(dnb_metadata)

        result = str(dnb_metadata)
        sysout = open(out, 'w')
        sysout.write(result)


extract_data_from_dnb_download_files(isbnprefixes)
