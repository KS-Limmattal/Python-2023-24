#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Erzeugen Sie ein Wörterbuch, welches jeder ganzen Zahl im Intervall [-7, 7] das Quadrat zuordnet und geben
Sie die Anzahl Schlüssel dieses Wörterbuchs in einem sauber formatierten Satz aus.

Lösungsversuch:
"""
dict = {n: n**2 for n in range(-7, 8)}
# der Zahl n muss das Quadrat zugeordnet werden, nicht umgekehrt
print(f"Das Wörterbuch hat {len(dict.keys())} Schlüssel")
