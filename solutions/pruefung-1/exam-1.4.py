#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Prüfungsaufgabe 4 (vom 24.11.2021)
Gegeben ist eine Liste von Tiernamen. Erzeugen Sie daraus ein Wörterbuch, in welchem jedem Tiernamen eine
zufällige Ganzzahl zwischen 3 und 10 (inklusive der Grenzen 3 und 10) zugeordnet wird und geben Sie dieses aus.
Schreiben Sie darauf für jedes Schlüssel-Werte Paar im Wörterbuch einen Satz hin wie:

'Der Tiername Esel besteht aus weniger als 7 Buchstaben' (wenn dem Esel die Zahl 7 zugeordnet wurde) bzw.
'Der Tiername Affe besteht aus genau 4 Buchstaben' (wenn dem Affen die Zahl 4 zugeordnet wurde) bzw.
'Der Tiername Giraffe besteht aus mehr als 3 Buchstaben' (wenn dem Giraffen die Zahl 3 zugeordnet wurde)
...

und erstellen Sie darauf eine Liste bestehend aus allen Tiernamen, die auf die zugeordnete Anzahl Buchstaben
gekürzt oder mittels des Zeichens "_" verlängert werden
("Esel" wird verlängert zu "Esel___", "Giraffe" gekürzt zu "Gir" im obigen Beispiel)
"""
# VORGEGEBENER TEIL (bitte nicht abändern)
from random import randint

li = [
    "Esel",
    "Affe",
    "Giraffe",
    "Krokodil",
    "Löwe",
    "Emu",
    "Katze",
    "Chamäleon",
    "Bartgeier",
]
# ENDE VORGEGEBENER TEIL

# BEGINN DES EIGENTLICHEN PROGRAMMS (bitte ergänzen)

zufallsbuch = {x: randint(3, 10) for x in li}
print(zufallsbuch)
li2 = []

for name, val in zufallsbuch.items():
    if len(name) < val:
        print(f"Der Tiername {name} besteht aus weniger als {val} Buchstaben")
        li2.append(name + (val - len(name)) * "_")
    elif len(name) > val:
        print(f"Der Tiername {name} besteht aus mehr als {val} Buchstaben")
        li2.append(name[:val])
    else:
        print(f"Der Tiername {name} besteht aus genau {val} Buchstaben")
        li2.append(name)

print(li2)
