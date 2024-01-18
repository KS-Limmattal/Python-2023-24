#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nachprüfung Aufgabe 4 (vom 1.12.2023)

Gegeben ist Liste 

li = ["Agrarwesen", "Rathaus", "Hallo", "Manjaro", "Saranna", "Katana", "Ranger", "Rallentando", "Kashmir", "Araber", "Handgranate", "Kino", "Musikant", "Hund", "Karaoke", "Affentante", "Magier", "Heldenmut"]

Erzeugen Sie ein Wörterbuch, welches jedem Wort aus der obigen Liste eine Liste bestehend aus den
Positionen des Buchstabens "a" (egal ob klein- oder grossgeschrieben) in diesem Wort zuordnet
und geben Sie das Wörterbuch aus.

Zum Beispiel müsste dem Wort "Agrarwesen" die Liste [1, 4] zugeordnet werden, da der Buchstabe "a" an
erster und vierter Position in diesem Wort auftaucht.
"""

li = [
    "Agrarwesen",
    "Rathaus",
    "Hallo",
    "Manjaro",
    "Saranna",
    "Katana",
    "Ranger",
    "Rallentando",
    "Kashmir",
    "Araber",
    "Handgranate",
    "Kino",
    "Musikant",
    "Hund",
    "Karaoke",
    "Affentante",
    "Magier",
    "Heldenmut",
]

dict = {}
for wort in li:
    pos = []
    for i, letter in enumerate(wort):
        if letter.lower() == "a":
            pos.append(i + 1)
    dict[wort] = pos

print(dict)
