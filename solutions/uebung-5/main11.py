#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Lassen Sie den Benutzer 5 ganze Zahlen eingeben, speichern Sie diese in einer Liste ab
und geben Sie darauf das grösste Element dieser Liste in einem sauber formatierten Satz aus.

Lösungsversuch:
"""
li = []
N = 5

print("Geben Sie im Folgenden bitte 5 ganze Zahlen (wie 2, -5, 13, -4, 8) ein")
for i in range(1, N + 1):
    n = int(input(f"Geben Sie die {i}. Ganzzahl ein: "))
    li.append(n)

largest = li[0]  # Es können auch alle eingegebenen Zahlen negativ sein
for n in li:
    if n > largest:
        largest = n

print(f"Das grösste Element der Liste {li} ist {largest}")
