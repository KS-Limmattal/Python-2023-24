#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Lassen Sie den Benutzer eine komplexe Zahl eingeben. Geben Sie danach in einem sauber formatierten Satz aus, ob die
eingegebene Zahl reell ist.

Lösungsversuch:
"""
z = complex(input("Geben Sie bitte eine komplexe Zahl in der Form a+bj ein: "))
if z.imag == 0:  # Eine Zeichenkette wie 4+0j enthält auch das Symbol "j"
    print(f"Die eingegebene Zahl {z} ist nicht reell.")
else:
    print(f"Die eingegebene Zahl {z} ist reell.")
