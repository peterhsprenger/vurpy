# -*- coding: iso-8859-1 -*-

import os
#import subprocess
import re
#import string

dump_data = []
dump_data_path = "F:\UTBeScholars\LIEFERUNG\Inhaltsverzeichnisse\TMP"
bookmarks = {}


# Zusammenstellung aller Dateien im Verzeichnis zu weiteren Bearbeitung; es werden die Dateinamen ohne Pfad ausgegeben
for dd in os.listdir(dump_data_path):
    if os.path.isfile(os.path.join(dump_data_path, dd)):
        #pdf_files_path.append(os.path.join(dump_data_path, dd)) 
        dump_data.append(dd)


print 'Dump Data', dump_data
print 'Length Dump Data', len(dump_data)
print 'Bookmarks Dictionary', bookmarks


# zunächst werden aus den mit pdftk erzeugten Dateien für jedes verfügbare PDF die Bookmarks für die Table of Contents ausgelesen
for dd in dump_data:
    o_dd = open(os.path.join(dump_data_path, dd))
    r_dd = o_dd.read()
    f_dd = re.findall('BookmarkTitle: Table of Contents\sBookmarkLevel: [0-9]\sBookmarkPageNumber: ([0-9]+)\sBookmarkBegin\sBookmarkTitle: Body\sBookmarkLevel: [0-9]\sBookmarkPageNumber: ([0-9]+)', r_dd)        
    
    # vor der Zusammenführung muss die Seitenzahl der letzten Seite eines Inhaltsverzeichnisses um den Wert "1" verringert werden 
    # (es hört ja auf der Seite VOR dem nächsten Bookmark auf!) 
    for x, y in f_dd:
        pp = int(x), int(y) - 1
    
    # aus dem Dateinamen wird die ISBN extrahiert für das spätere Dictionary mit ISBN-Seitenzahl-Paaren
    isbn = re.findall('(\d\d\d\d\d\d\d\d\d\d\d\d\d).*', dd)

    
    print "DD", dd
    print "FDD", f_dd
    print "PP", pp
    print "ISBN", isbn
    bookmarks_tmp = []
    bookmarks_tmp.append(isbn)
    print "Bookmarks_TMP", bookmarks_tmp
    print "Seitenzahl", f_dd

    for isbn in bookmarks_tmp[0]:
        #print "Bookmark", isbn
        if isbn not in bookmarks:
            bookmarks[isbn] = pp
    
  
print 'Bookmarks Dictionary - neu:', bookmarks

