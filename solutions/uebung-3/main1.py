#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Schreiben Sie ein Programm, welches die Eulersche Zahl e = 1 + 1/1! + 1/2! + 1/3! + ... 
auf eine vom Benutzer vorgegebene Nachkommastellen-Anzahl genau berechnet. Arbeiten Sie dazu mit 
Ganzzahl-Arithmetik

Beispiel: Eingabe (für Nachkommastellen-Anzahl) 5; Ausgabe: e=2.71828
"""

N = int(input("Wie viele Nachkommastellen der Eulerschen Zahl sollen berechnet werden? N = "))
extra = 2   # Zusätzliche Stellen, mit denen gerechnet werden (könnte abhängig von N abgeschätzt werden)
s = 10 ** (N + extra)
e = s
i = 0

while s > 0:
    i += 1
    s //= i  # Ganzzahl-Division
    e += s

print(f"Die Eulersche Zahl auf {N} Nachkommastellen: e =  {e // 10**(N+extra)}.{(e - 2*10**(N+extra)) // 10**extra}")
