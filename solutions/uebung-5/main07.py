#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Lassen Sie den Benutzer eine ganze Zahl eingeben. Schreiben Sie je nach Eingabe den passenden Satz
"Die eingebene Zahl ist gerade" bzw. "Die eingegebene Zahl ist ungerade" hin.

Lösungsversuch:
"""
n = int(input("Geben Sie eine ganze Zahl ein: n = "))

if n % 2 == 0:  # Der Vergleichsoperator ist "==", der Zuweisungsoperator "="
    print("Die eingegebene Zahl ist gerade")
else:
    print("Die eingegebene Zahl ist ungerade")
