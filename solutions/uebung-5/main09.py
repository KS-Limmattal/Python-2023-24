#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Starten Sie mit der Liste li = [4, 2, 5, 6, 7, 19, 23, 4, 7, 2, 16] und geben Sie sie aus.
Lassen Sie den Benutzer eine ganze Zahl eingeben. Ist die Zahl in der Liste enthalten, so
entfernen Sie so lange das letzte Listenelement, bis die Liste die eingegebene Zahl nicht 
mehr enthält und geben Sie darauf die verkürzte Liste aus.
Andernfalls geben Sie "Die Zahl ist nicht in der Liste enthalten" aus.

Lösungsversuch:
"""
li = [4, 2, 5, 6, 7, 19, 23, 4, 7, 2, 16]
print(li)

n = int(input("Geben Sie eine ganze Zahl ein: n = "))
if n in li:
    while n in li:
        li = li[0 : len(li) - 1]  # Das letzte Listenelement ist an Position len(li) - 1
    print(li)
else:
    print("Die Zahl ist nicht in der Liste enthalten")
