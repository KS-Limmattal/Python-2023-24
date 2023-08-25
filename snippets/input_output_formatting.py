#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ausgabe, Eingabe und Formattierung

# Input als Zeichenkette (string)
name = input("Wie heisst du? ")
# Input als Ganzzahl (int) interpretiert
age = int(input("Wie alt bist du (in Jahren)? "))
# Input als Fliesskommazahl (float) interpretiert
height1 = float(input("Wie gross bist du (in cm)? "))
height2 = float(input("Wie gross warst du bei der Geburt (in cm)? "))

# Formattierung als f-string; Ausgabe auf 2 Nachkommastellen
print(f"{name}, pro Lebensjahr bist du durchschnittlich {(height1-height2)/age:.2f} cm gewachsen")
