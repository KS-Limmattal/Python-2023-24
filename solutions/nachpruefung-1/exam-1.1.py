#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nachprüfung Aufgabe 1 (vom 1.12.2023)

Berechnen Sie die Laplace-Wahrscheinlichkeit dafür, dass in einer 2x2-Matrix [[a,b], [c,d]] mit 4 zufälligen
ganzzahligen Einträgen a,b,c,d im Intervall [-5, 5] sowohl Determinante a*d-b*c wie auch Spur a+d verschieden 
von 0 sind und geben Sie diese Wahrscheinlichkeit als Prozentzahl gerundet auf 3 Nachkommastellen in einem sauber
formatierten Satz aus.
"""

guenstige = 0
moegliche = 0
for a in range(-5, 6):
    for b in range(-5, 6):
        for c in range(-5, 6):
            for d in range(-5, 6):
                moegliche += 1
                det = a*d-b*c
                spur = a + d
                if det!=0 and spur!=0:
                    guenstige += 1

print(f"Die gesuchte Wahrscheinlichkeit beträgt {100*guenstige/moegliche:.3f}%")