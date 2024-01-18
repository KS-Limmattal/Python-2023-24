#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nachprüfung Aufgabe 2 (vom 1.12.2023)

Schreiben Sie ein Programm, welche ein reelles quadratisches Polynom a*x^2 + b*x + c mittels Eingabe der
Koeffizienten abfragt und dann die reellen Nullstelle(n) des Polynoms in einem sauber formatierten Satz 
wie "Das Polynom 1.0*x^2 + -3.0*x + 2.25 hat die reelle Nulstelle 1.5" ausgibt, bzw. die Information, dass keine reelle Nullstellen existieren.
"""

from math import sqrt
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - 4*a*c
start = f"Das Polynom {a}*x^2 + {b}*x + {c} hat"

if D>0:
    x1 = (-b + sqrt(D))/(2*a)
    x2 = (-b - sqrt(D))/(2*a)
    print(f"{start} die reellen Nullstellen {x1} und {x2}")
elif D==0:
    x = -b/(2*a)
    print(f"{start} die reelle Nullstelle {x}")
else:
    print(f"{start} keine reellen Nullstellen")