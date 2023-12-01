#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Generieren Sie eine Liste bestehend aus 10 (ganzer) Zufallszahlen im Intervall [0, 10] und geben Sie
in einem sauber formatierten Satz das Maximum und das Minimum der Liste aus.

Lösungsversuch:
"""
import random as rnd

li = []
li = [rnd.randint(0, 10) for i in range(10)]
# "==" ist der Vergleichsoperator, hier soll (mit "=") zugewiesen werden
largest = max(li)
lowest = min(li)

print(f"Das grösste Element der Liste {li} lautet {largest}, das kleinste {lowest}")
