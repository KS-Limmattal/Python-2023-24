#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Lass den Benutzer eine ganze Zahl n >= 0 eingeben. Berechne darauf die Zahl (2n+1)! und gib sie aus.

Lösungsversuch:
"""
n = int(input("Geben Sie eine ganze Zahl n >= 0 ein: "))

faktor = 1
fakultaet = 1

for i in range(n):
    faktor += 2
    fakultaet *= (faktor - 1) * faktor  # Hier gingen die geraden Faktoren vergessen

print(f"{2*n+1}! = {fakultaet}")
