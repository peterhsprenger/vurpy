# -*- coding: iso-8859-1 -*-

import os
from os import *
import subprocess
import re
pdftk = 'C:\\Program Files\\PDF Software\\PDFtk Server\\bin\\pdftk.exe'

pdf_files = []
pdf_files_path = []
pdf_path = 'F:\\UTBeScholars\\LIEFERUNG\\eBooks'

for f in os.listdir(pdf_path):
    if os.path.isfile(os.path.join(pdf_path, f)):
        #pdf_files_path.append(os.path.join(pdf_path, f)) 
        pdf_files.append(f)
print pdf_files
print len(pdf_files)
# print pdf_files_path
# print len(pdf_files_path)

# escholar = ['F:\\UTBeScholars\\LIEFERUNG\\eBooks\\9783647310251.pdf', 'F:\\UTBeScholars\\LIEFERUNG\\eBooks\\9783847003533.pdf', 'F:\\UTBeScholars\\LIEFERUNG\\eBooks\\9783647404615.pdf']
# escholar = os.listdir('F:\\UTBeScholars\\LIEFERUNG\\eBooks')


# durchlaufe die Dateien im Verzeichnis und call sejda tools and split document
# splitted = []

# Die eBooks werden durchsucht und es wird an dem Bookmark beginnend mit "Table" gesplitted und in ein Verzeichnis TMP gelegt


targetpath_tmp = 'F:\\UTBeScholars\\LIEFERUNG\\Inhaltsverzeichnisse\\TMP\\'

for pdf in pdf_files:
    call = pdftk
    call += " "
    call += os.path.join(pdf_path, pdf)
    call += ' dump_data_utf8 output '
    call += targetpath_tmp
    call += str(pdf) + ".txt"
    print '\n', call
    subprocess.call(call)
    print '\nPDFtk generated dump_data File successfully'

print 'PDFtk has completed.\n\n'