#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe: 
Berechne die Wurzel von 2 mit Hilfe des Heron-Verfahrens x_{n+1} = 1/2*(x_n + 2/x_n)
und Startwert x_0 = 1. Führe dazu 10 Schritte aus und gib das Resultat auf 5-Nachkommastellen aus.

Lösungsversuch:
"""
wurzel2 = 1
for i in range(10):
    wurzel2 = 1 / 2 * (wurzel2 + 2 / wurzel2)

print(f"Wurzel(2) = {wurzel2}")

# In Funktionsnamen dürfen nur buchstaben und ziffern, sowie der Unterstrich _ vorkommen
# Die runden Klammern () sind für Funktionsaufrufe reserviert
