#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Starten Sie mit einer leeren Liste und lassen Sie den Benutzer wiederholt eine Zahl eingeben. 
Ist die Zahl noch nicht in der Liste, fügen Sie sie hinzu. Ist die Zahl hingegen bereits in der Liste,
so beenden Sie das Programm und verabschieden den Benutzer

Lösungsversuch:
"""
li = []

while True:
    n = int(input("Geben Sie eine ganze Zahl ein: "))
    if n not in li:
        li.append(n)
    else:  # Die Liste wird im ersten Fall durch n ergänzt, so dass "n in li" automatisch eintreten würde
        break

print("Ciao!")
