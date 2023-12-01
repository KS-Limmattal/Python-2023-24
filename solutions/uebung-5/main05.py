#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Lassen Sie den Benutzer eine komplexe 2x2-Matrix eingeben und geben Sie sie aus

Lösungsversuch:
"""
import numpy as np

print("Geben Sie eine komplexe 2x2-Matrix mittels ihrer Einträge in der Form a+bj ein")
a11 = complex(input("a11 = "))
a12 = complex(input("a12 = "))
a21 = complex(input("a21 = "))
a22 = complex(input("a22 = "))

A = np.array([[a11, a12], [a21, a22]])
print(A)

# Der input muss in eine komplexe Zahl konvertiert werden, nicht umgekehrt
