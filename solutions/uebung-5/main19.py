#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Erzeugen Sie zuerst die Liste aller Quadratzahlen von 1^2 bis 30^2. 
Entfernen Sie danach die Quadratzahl 225 aus der Liste und geben Sie die neue Liste aus.

Lösungsversuch:
"""
li = [n**2 for n in range(1, 31)]
# Eine Potenz a^r wird in Python als a**r geschrieben
li.remove(225)
print(li)
