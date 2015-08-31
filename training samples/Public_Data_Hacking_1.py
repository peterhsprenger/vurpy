# -*- coding: iso-8859-1 -*-

# The Traveling Suitcase Problem: in einem Chaicagoer Bus wurde soeben eine Tasche liegengelassen. Mit diesem Programm soll herausgefunden werden
# ... in welchem Bus die Tasche vermutlich liegt und wann dieser Bus sich auf der Rückrpute wieder in der Nähe befindet, sodass man...
# ... die Tasche eventuell direkt aus dem Bus holen kann, statt darauf zu warten, bis die Tasche im Fundbüro abgegeben wurde. 

# FIND THE RIGHT BUS

# im folgenden Code wird zunächst die Bibliothek zum Import von Daten aus einer URL geladen und anschließend werden die Daten der Quelle...
# ... hier der Chicago Transit Authority für die Buslinie 22 geladen, danach die Daten in einer Variable eingelesen, 
# ... danach werden die eingelesenen Daten in eine vorher erzeugte XML-Datei geschrieben und anschließend diese Datei geschlossen.
import urllib
url_open = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')     # Aufruf der Datenquelle
url_data = url_open.read()    # Einlesen der Daten als String in eine Variable
write_data_in_file = open('publicDataHacking/rt22.xml', 'wb')   # Anlegen einer Datei, in der die Daten gespeichert werden
write_data_in_file.write(url_data)      # Daten in die Datei schreiben
write_data_in_file.close()      # Datei schließen

# Die beiden folgenden Variablen definieren den Standort von Dave, der die Tasche vergessen hat. Sie sind die Berechnungsgrundlage ...
# ... dafür, welcher Bus in Frage kommt (weil es ein spezieller Bus der Linie 22 sein muss, der erst vor wenigen Minuten ...
# ... ungefähr diese Koordinaten hatte, als Dave ausgestiegen ist) und wann dieser Bus diese Koordinaten auf seiner umgekehrten Tour...
# ... wieder erreicht, damit Dave im Bus nach seiner Tasche gucken kann. Die Angaben sind Längen- und Breitengrade 
daves_lat = 41.980262
daves_long = -87.668452

# Die heruntergeladenen Daten enthalten alle Details zu allen aktuell fahrenden Bussen der Linie 22 in einer XML-Datei. 
# ... Die XML-Datei wird kontinuierlich aktualisiert, wenn wir sie in einem regelmäßigen Rhythmus herunterladen.
# ... Zur Analyse der XML-Datei wird das Modul xml.etree geladen und die Methode parse importiert
# ... Das Programm liest (parsed) jetzt diese XML-Datei nach den für das Problem relevanten Informationen:
# ... das XML-Element d = "direction" und lat = Latitude
# ... der folgende Programmcode dient nur dazu, die Daten aller Buslinien zu lesen - und löst das Problem noch nicht (nur zur Veranschaulichung)
from xml.etree.ElementTree import parse
doc = parse('publicDataHacking/rt22.xml')
for bus in doc.findall('bus') :
    var_id_all = bus.findtext('id')
    var_d_all = bus.findtext('d')
    var_lat_all = float(bus.findtext('lat'))
#    print var_id, var_d, var_lat
    
# Mit diesem Programmteil wird nun genauer ermittelt, welcher der Busse dafür in Frage kommt, dass Dave seine Tasche darin vergessen hat.    
candidates = list()
print 'Kandidaten vor Ermittlung:', candidates
for bestbus in doc.findall('bus') : 
    var_lat = float(bus.findtext('lat'))
    if var_lat > daves_lat :                    # Der Bus muss sich momentan weiter nordwärts bewegen (denn das war die Richtung des Busses; also ist der Breitengrad größer als der von Daves Position
        direction = bus.findtext('d')
        if direction.startswith('North') :      # Der Bus muss außerdem in nördlicher Richtung sein, nicht in südlicher Richtugn (selbst wenn er sich noch nördlich von Dave befindet), denn Daves Bus fuhr Richtung Norden
            busid = bus.findtext('id')
            candidates.append(busid)            # Die in Frage kommenden Busse werden an eine Liste übergeben, damit sie weiter beobachtet werden können
            print 'Kandidaten nach Ermittlung:', candidates(busid, var_lat)      # Von den in Frage kommenden Bussen werden nun die IDs und der Breitengrad ausgegeben


def distance(lat1, lat2) :                      # definierte eine Funktion für zwei Lägengrad-Variablen
    return 69 * abs(lat1 - lat2)                # mit dieser Funktion wird grob berechnet, wie viele Meilen der Bus momentan entfernt ist 

# MONITOR THE BEST BUS

def monitor() :
    url_open = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')     # Aufruf der Datenquelle
    doc = parse(url_open)
    for bus in doc.findall('bus') : 
        busid = bus.findtext('id')
        if busid in candidates :
            var_lat = float(bus.findtext('lat'))
            dist = distance(var_lat, daves_lat)
            print 'Aktuelle Info zum Buskandidaten:', busid, dist, 'miles'
    print '-' * 10
                        
    
import time
while True :
    monitor()
    time.sleep(60)
