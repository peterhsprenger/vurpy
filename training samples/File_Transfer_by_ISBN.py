# -*- coding: iso-8859-1 -*-

# Hier wird das OS-Modul geladen, dass den Zugriff auf Betriebssystemvariablen 
# und das Modul shutil, das spezifische Betriebssystemoperatione in Python unterstuetzt

import os
cwd = os.getcwd()
print cwd
import shutil
from Tkinter import *
from tkMessageBox import *
from tkFileDialog   import askopenfilename

# Hier werden die Variablen zu Abarbeitung des Programms durch den User angegeben werden: 
# die Quelldatei mit der ISBN-Liste, das Quellverzeichnis und das Zielverzeichnis
# Für den Fall einer fehlenden Angabe wird ein vorgegebenes Standardverzeichnis benutzt 

def Datenquelle():
    quelle = askopenfilename()
    print quelle
    
#tk_chooseDirectory
sourceList = Button(text='Quelldatei auswählen', command=Datenquelle).pack(fill=X)
mainloop()

print sourceList
#source_list = raw_input("Bitte geben Sie den Namen und den Pfad der Datei an, in der die zu verschiebenden Dateien stehen. ")
if len(source_list) == 0:
    source_list = 'c:/test/isbn.txt'
source_dir = raw_input("Bitte geben Sie an, in welchem Verzeichnis die zu kopierenden Dateien liegen") 
if len(source_dir) == 0:
    source_dir = 'c:/test/'
target_dir = raw_input("Bitte geben Sie an, in welches Verzeichnis die Dateien kopiert werden soll")
if len(target_dir) == 0:
    target_dir = 'c:/test/target/'
source = open(source_list)
for line in source :
    isbn = line.strip() + ".pdf"
    isbn_file = os.path.join(source_dir, isbn)
    shutil.copy(isbn_file, target_dir)
    print "Datei", isbn_file, "erfolgreich in das Zielverzeichnis", target_dir, "kopiert"
print "Alle Kopiervorgaenge abgeschlossen"