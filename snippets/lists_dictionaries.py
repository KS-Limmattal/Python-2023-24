#!/usr/bin/env python3
# -*- coding: utf-8 -*-

li = ["Wort", 1, "noch eine Zeichenkette", 23.4]  # Eine Liste
li.append("Noch ein Listeneintrag")
li += ["Eine", "ganze", "Reihe", "von", "neuen", "Listeneinträgen"]
li += "Hänge die Wörter dieses Satzes an".split()  # Leerzeichen als Trennungszeichen
print(li)

# Iteration durch eine Liste
for s in li:
    print(s)

# mit Aufzählung der Elemente
for n, s in enumerate(li):
    print(f"Der {n+1}. Listeneintrag lautet: {s}")


# Elegante Listenerzeugung
Zweierpotenzen = [2**n for n in range(20)]
QuadrateUngeraderZahlen = [n**2 for n in range(20) if n % 2 == 1]

# Ein Wörterbuch (dictionary) besteht aus Paaren von Schlüssel und zugeordnetem Wert
week_day_dict = {
    1: "Montag",
    2: "Dienstag",
    3: "Mittwoch",
    4: "Donnerstag",
    5: "Freitag",
    6: "Samstag",
    7: "Sonntag",
}
print(f"Der 4. Wochentag ist der {week_day_dict[4]}")

deutsch_franz_dict = {
    "gelb": "jaune",
    "rot": "rouge",
    "blau": "bleu",
    "grün": "vert",
    "weiss": "blanche",
}
franz_engl_dict = {
    "jaune": "yellow",
    "rouge": "red",
    "bleu": "blue",
    "vert": "green",
    "blanche": "white",
}

for col in deutsch_franz_dict:
    print(
        f"""
          Die Farbe {col} heisst auf Französisch {deutsch_franz_dict[col]} 
          und auf Englisch {franz_engl_dict[deutsch_franz_dict[col]]}
          """
    )

# Ein Wörterbuch einhängen; existierende Schlüssel werden mit den neuen Werten überschrieben
deutsch_franz_dict.update({"schwarz": "noir", "weiss": "blanc"})

for d, f in deutsch_franz_dict.items():
    print(f"{d} = {f}")


import numpy as np
import random as rnd

dir_dict = {
    "left": np.array([-1, 0]),
    "right": np.array([1, 0]),
    "up": np.array([0, -1]),
    "down": np.array([0, 1]),
}

pos = np.array([5, 12])
pos = pos + 3 * dir_dict["up"]  # Macht 3 Schritte nach oben

keys = list(dir_dict.keys())
dir = np.random.choice(keys)  # Zufallsauswahl eines Listenelements
pos = pos + dir_dict[dir]  # macht einen Schritt in zufälliger Richtung

# split: trennt strings beim Leerzeichen
text = "Das ist ein Satz"
text.split()
# gibt ['Das', 'ist', 'ein', 'Satz']

# len() gibt die Länge von einem String (Anzahl zeichen) oder einer Liste (anzahl Einträge in der Liste) an
name = "Roland"
len(name)
# gibt 6

liste = ["loe", "bnd", "wnk", 2, 3]
len(liste)
# gibt 5
