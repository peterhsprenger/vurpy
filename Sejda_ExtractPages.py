# -*- coding: iso-8859-1 -*-

#import os
#from os import *
import subprocess
#import re
#from read_PDFtk_dumpdata import isbn

sejda = raw_input("Geben Sie das Verzeichnis an, in dem sich die sejda-console befindet:")
if len(sejda) == 0:
    sejda = 'C:\\sejda-console-1.0.0.M9-bin\\bin\\sejda-console.bat'


quelle = {'9783647404615': (6, 9), '9783647402307': (6, 9), '9783847003458': (5, 8), '9783847003786': (5, 8), '9783847003670': (5, 6), '9783847003397': (7, 10), '9783847003892': (5, 6), '9783647369983': (6, 7), '9783847003724': (5, 6), '9783847002987': (5, 6), '9783847003854': (5, 8), '9783647310251': (6, 7), '9783847003175': (5, 8), '9783647300689': (6, 7), '9783847003519': (7, 10), '9783847003007': (5, 6), '9783647317151': (6, 7), '9783847003052': (5, 6), '9783647370354': (6, 9), '9783847003717': (5, 6), '9783847002895': (5, 6), '9783847003106': (5, 6), '9783647370347': (8, 13), '9783847003533': (11, 24), '9783847003120': (5, 6), '9783847003274': (5, 6), '9783847103097': (5, 8), '9783647451886': (6, 7), '9783647403656': (6, 7), '9783847003304': (5, 8), '9783847002352': (5, 6), '9783647301716': (6, 9), '9783847003960': (7, 12), '9783847003144': (5, 6), '9783647402468': (8, 11), '9783647300726': (6, 11), '9783847003168': (5, 6), '9783647253220': (6, 9), '9783647369976': (6, 7), '9783847003366': (5, 10), '9783847000709': (5, 6), '9783647301693': (8, 11), '9783847003243': (7, 8), '9783647403410': (6, 9), '9783847003526': (7, 10), '9783847002307': (5, 8), '9783847003625': (5, 6), '9783847003403': (5, 8), '9783847003359': (5, 8), '9783647462141': (6, 9), '9783647301709': (6, 7), '9783647370330': (6, 7), '9783847003465': (5, 8), '9783647253053': (8, 11), '9783847003434': (5, 8), '9783647300382': (5, 9), '9783847003328': (5, 8), '9783847003250': (5, 6), '9783847103110': (5, 6), '9783847003137': (7, 8), '9783847003311': (5, 8), '9783647310237': (6, 7), '9783847003427': (5, 6), '9783647360799': (6, 7), '9783847003212': (7, 8), '9783647450216': (6, 7), '9783847003410': (5, 8), '9783647300566': (6, 7), '9783847002536': (7, 10), '9783647402437': (6, 7), '9783647403700': (6, 7), '9783647300559': (6, 7), '9783647300719': (6, 7)}
sourcepath = 'F:\\UTBeScholars\\LIEFERUNG\\eBooks\\'
targetpath = 'F:\\UTBeScholars\\LIEFERUNG\\Inhaltsverzeichnisse\\'    


for isbn, pp in quelle.items():
    pages = str(pp[0])+"-"+str(pp[1])
    call = sejda
    call += ' extractpages'
    call += ' -f '
    call += sourcepath
    call += isbn
    call += '.pdf'
    call += ' -o '
    call += targetpath
    call += 'IV_'
    call += isbn
    call += '.pdf'
    call += " -s "
    call += pages
    #call += '--overwrite'
    print '\n', call
    subprocess.call(call)
    print '\nIV erstellt\n\n'
        
print "Alle Dateien bearbeitet, die Inhaltsverzeichnisse befinden sich im Ordner", targetpath
