#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Geben Sie mit Hilfe einer Schleife für die Zahlen 1,2,...,10 die Fakultäten und Wurzeln der Zahlen
(gerundet auf 2 Nachkommastellen) in Sätzen der Form "Die Fakultät der Zahl 5 ist 120, die Wurzel 2.24" aus.

Lösungsversuch:
"""
import math as m

N = 10
for i in range(1, N + 1):
    print(f"Die Fakultät der Zahl {i} ist {m.factorial(i)}, die Wurzel {m.sqrt(i):.2f}")

# Das "!"-Zeichen kann in Python nicht für Fakultät verwendet werden
