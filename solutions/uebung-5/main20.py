#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Starten Sie mit der Liste aller Kleinbuchstaben ["a", "b", ..., "z"] im lateinischen Alphabet.
Geben Sie danach die um den ersten und letzten Kleinbuchstaben verkürzte Liste aus.

Lösungsversuch:
"""
li = [chr(97 + i) for i in range(26)]  # chr(97) = 'a', chr(98) = 'b', ... (ASCII-Codes)
li = li[1:25]  # Die Zuweisung fehlte
print(li)
