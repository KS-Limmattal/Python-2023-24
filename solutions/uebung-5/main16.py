#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Erzeugen Sie die Liste [2, -4, 8, -16, 32, ...] der ersten 20 Zweierpotenzen mit alternierenden Vorzeichen.
Verwenden Sie dabei Zwischenergebnisse, um effizienter zu rechnen.

Lösungsversuch:
"""
li = []
power = 2
sign = -1
for i in range(20):
    li.append(power)
    power *= sign * 2  # Der Vorzeichenwechsel ist hier schon eingebaut

print(li)
