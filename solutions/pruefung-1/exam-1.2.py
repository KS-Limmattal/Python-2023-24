#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Prüfungsaufgabe 2 (vom 24.11.2021)

Schreiben Sie ein Programm, welches dem Benutzer erlaubt, eine komplexe 2x2 Matrix einzugeben.
Geben Sie dann in einem Satz aus, ob das Quadrat dieser Matrix reell ist und geben Sie im Falle, 
dass das Matrix-Quadrat reell ist, den grössten Eintrag des Matrix-Quadrats aus.

Beispiel:
    Benutzereingabe: Matrix [[1+1j, 1+2j], [1-4j, -1-1j]]
    Ausgabe: 'Das Matrix-Quadrat ist reell und der grösste Eintrag davon lautet 9.0'
"""

import numpy as np

a11 = complex(input("a11 = "))
a12 = complex(input("a12 = "))
a21 = complex(input("a21 = "))
a22 = complex(input("a22 = "))
A = np.array([[a11, a12], [a21, a22]])
Sq = A @ A

if np.all(Sq.imag == 0):
    print(
        f"Das Matrix Quadrat ist reell und der grösste Eintrag davon lautet {np.max(Sq.real)}"
    )
else:
    print("Das Matrix-Quadrat ist nicht reell")
