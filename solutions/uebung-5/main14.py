#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Überlegen Sie sich, weshalb die Zahl 29! durch eine Million teilbar ist. 
Geben Sie die letzten 3 Ziffern des Quotienten in einem sauber formatierten Satz aus.

Lösungsversuch:
"""
from math import factorial

dividend = factorial(29)
divisor = 1_000_000
quotient = dividend // divisor  # Hier wird Ganzzahl-Division gebraucht
digits = str(quotient)[-3:]
print(
    f"Die letzten 3 Ziffern des Quotienten von {dividend} durch {divisor} sind {digits}"
)
