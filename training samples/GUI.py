# Video-Tutotial dazu: https://www.youtube.com/watch?v=hLXUaGvlIdE

# Importieren der Tkinter-Widgets
from Tkinter import *
# Import der "Theme TKinter" Widgets, die Buttons etc mehr nach Windows 7/8 aussehen lassen
from ttk import *


# Das Hauptfenster wird erzeugt
window_main = Tk()                              
# Der Fenstertitel wird festgelegt
window_main.title("PDF-Dateien kopieren")       
# Die Groesse des anzuzeigenden Fensters wird festgelegt (Breite x Hoehe)
window_main.geometry("800x400")                 



# Damit ein Button-Element im Fenster etwas tun kann, muss die entsprechende Funktion VOR dem Button im Skript stehen
def ausgabe() :                                     
    print "Hallo"

# ein Button wird im Fenster angezeigt, der Button verweist auf die angelegte Funktion "ausgabe"
button_ok = Button(window_main, text = "Zeigt Hallo auf der Konsole an", command=ausgabe)      
# die Methode pack platziert den Button automatisch
button_ok.grid(row=1, column=1)                                

# Entry erzeugt ein Eingabefeld
eingabe = Entry(window_main)                    
eingabe.grid()

# Label erzeugt ein Ausgabefeld
label1 = Label()
label1.grid()

label2 = Label()
label2.grid()

def lesen():
    # hier wird eine Funktion erzeugt, die den Text aus dem Eingabefeld mit der Methode get im Labelfeld anzeigt
    label1.configure(text="Der eigegebene Wert lautet: " + (eingabe.get()))      
    
# mit dem Befehl command wird dem Button die Ausfuehrung der Funktion zugewiesen, hier der Funktion def=lesen
button2 = Button(window_main, text = "ich lese", command=lesen)     
button2.grid()

def rechnen():
    try:
        x = int(eingabe.get())
        # In dem Labelfeld koennen feste Texte, Wiedergabewerte, Variablen oder Berechnungen angezeigt werden
        label2.configure(text=(x**3))
    except:
        label2.configure(text="Bitte geben Sie eine Zahl ein")


button2 = Button(window_main, text = "ich rechne", command=rechnen)
# mit der Methode place kann das Element (hier der Button positioniert werden
button2.place(relx=0.6, rely=0.8, width=200, height=50)     

# Damit das Fenster dauerhaft angezeigt wird und nicht nur extrem kurz, muss es Windows als dauerhafte Applikation angezeigt werden; hierfuer ist mainloop() vorgesehen
window_main.mainloop()
