#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Aufgabe:
Erzeuge die Liste li, die (mit Auslassung) folgende Gestalt hat: ["Quadratzahlen", 1, 4, 9, ... , 900] 

Lösungsversuch:
"""
li = []  # {} ist ein Wörterbuch, [] eine Liste
li.append("Quadratzahlen")
for n in range(1, 31):
    li.append(n**2)
