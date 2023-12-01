#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Berechne die Laplace-Wahrscheinlichkeit, dass beim Wurf dreier Würfel keine zwei die gleiche
Augenzahl zeigen, und gib sie in einem sauber formatierten Satz aus

Lösungsversuch:
"""
guenstige = 0
moegliche = 0

for x in range(1, 7):
    for y in range(1, 7):
        for z in range(1, 7):
            moegliche += 1
            if x != y and y != z and z != x:
                guenstige += 1

print(f"Die gesuchte Wahrscheinlichkeit beträgt {guenstige/moegliche*100:.2f}%")

# for x, y, z in range(1, 7) ist syntaktisch nicht korrekt
