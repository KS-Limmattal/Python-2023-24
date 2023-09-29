#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Schreiben Sie ein Programm mit folgender Eingabe/Ausgabe:
Eingabe: Eine natürliche Zahl
Ausgabe: "Die Zahl ... ist eine Primzahl" bzw.
         "Die Zahl ... ist keine Primzahl, denn sie hat den nicht-trivialen Teiler ..."

Zusatz: Versuchen Sie die Laufzeit des Programms zu optimieren
"""
# from math import sqrt

prim = True
n = int(input("Geben Sie eine natürliche Zahl ein: "))

if n==1: 
    print("Die Zahl 1 ist keine Primzahl")
else:
    for t in range(2, int(n**0.5)+1):
        if n % t == 0:
            prim = False
            print(
                f"Die Zahl {n} ist keine Primzahl, denn sie hat den nicht-trivialen Teiler {t}.")
            break

    if prim:
        print(f"Die Zahl {n} ist eine Primzahl")
