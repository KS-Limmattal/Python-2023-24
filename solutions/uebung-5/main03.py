#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Erzeuge eine Liste bestehend aus 10 Zufallszahlen (von Typ int) zwischen 2 und 8 (inklusive Grenzen) 
und gib sie aus.

Lösungsversuch:
"""
from random import randint

li = [randint(2, 8) for i in range(10)]
print(li)

# Hier wurde aus random bereits der Befehl `randint` importiert.
# Er kann bzw. muss direkt so verwendet werden
# rnd.randint würde nur passen, wenn mit `import random as rnd` importiert würde.
