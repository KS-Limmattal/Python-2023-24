#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Finden und korrigieren Sie den Fehler im folgenden Programmtext.
"""

from random import randint

max_n = 10
li = [n**2 for n in range(1, max_n + 1)]

print(f"Geben Sie jeweils die Zahl n ein, deren Quadrat die vorgegebene Zahl ist")

correct = 0
while True:
    index = randint(0, max_n - 1)
    # Der Index beginnt bei 0 und die Grenzen sind mit dabei
    square = li[index]
    n = int(input(f"n^2 = {square}, n = "))
    if n**2 == square:
        correct += 1
    else:
        print(f"Falsch, damit ist das Spiel bei {correct} richtigen Antworten beendet.")
        break
