#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Prüfungsaufgabe 1 (vom 24.11.2023)

Berechnen Sie die Zahl sin(1) auf 50 Nachkommastellen genau mittels der Reihe: 
    sin(1) = 1/1! - 1/3! + 1/5! - 1/7! +- ...

Verwenden Sie dabei Ganzzahl-Arithmetik mit 2 Extrastellen für Zwischenergebnisse und geben Sie
das Ergebnis inklusive der Anzahl verwendeter Summanden sauber formatiert auf 2 Zeilen aus, 
wie (spoiler: korrekter Ergebnis!)

'sin(1) = 0.84147098480789650665250232163029899962256306079837'
'Für die Berechnung wurden ?? Summanden gebraucht.' 

(Dabei ist in der 2. Zeile ?? durch die korrekte verwendete Anzahl Summanden zu ersetzen)
"""

N = 50  # Anzahl Nachkommastellen
extra = 2  # Anzahl Extrastellen für Zwischenergebnisse

sin = 0
num = 0  # Anzahl Summanden
summand = 10 ** (N + extra)  # aktueller Summand

while summand != 0:
    sin += summand
    num += 1
    summand //= -(2 * num) * (2 * num + 1)

print(f"sin(1) = 0.{sin // 10 ** extra}")
print(f"Für die Berechnung wurden {num} Summanden gebraucht.")
