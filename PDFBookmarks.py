# -*- coding: iso-8859-1 -*-
# -*- coding: latin-1 -*-
# -*- coding: utf-8 -*-

import os
import GetPDF_Bookmarks
import unicodedata


# in die leere Liste werden später alle PDF-ISBNs eingetragen
# in das leere Dictionary werden die zu einer PDF-ISBN Bookmarks zu den PDF-Dateien 
pdf_files = []
pdf_files_path = []
bookmarks = {}


pdf_sourcedir = raw_input("Geben Sie das Verzeichnis an, in dem sich die PDF-Dateien befinden: ")
if len(pdf_sourcedir) == 0:
    pdf_sourcedir = 'F:\UTBeScholars\LIEFERUNG\eBooks'

for f in os.listdir(pdf_sourcedir):
    if os.path.isfile:
        pdf_files.append(f)
        pdf_files_path.append(os.path.join(pdf_sourcedir, f))
print pdf_files
print pdf_files_path

'''
for pdf_file in pdf_files_path:
    pdf = GetPDF_Bookmarks.GetPDFBookmarks(open(pdf_file, 'rb'))
    template = '%-5s  %s'
    print template % ('page', 'title')
    for p,t in sorted([(v,k) for k,v in pdf.getDestinationPageNumbers().iteritems()]):
        print template % (p+1,t)

'''
'''        
for f in os.listdir(pdf_sourcedir):
    if os.path.isfile(os.path.join(pdf_sourcedir, f)):
        escholar.append(os.path.join(pdf_sourcedir, f))
print escholar
print len(escholar)
'''
    
#for pdf in os.listdir(pdf_sourcedir):

    
pdf = GetPDF_Bookmarks.GetPDFBookmarks(open("F:\UTBeScholars\LIEFERUNG\eBooks\9783647253053.pdf", 'rb'))
template = '%-5s  %s'
print template % ('page', 'title')
for p,t in sorted([(v,k) for k,v in pdf.getDestinationPageNumbers().iteritems()]):
    print template % (p+1,t)
        
