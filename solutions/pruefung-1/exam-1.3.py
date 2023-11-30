#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Prüfungsaufgabe 3 (vom 24.11.2021)

Sie beginnen mit einer leeren Liste.
Fordern Sie den Benutzer wiederholt zur Eingabe eines Namens (Zeichenkette) auf.
- Jedes Mal, wenn der eingegebene Namen in der Liste noch nicht enthalten ist, fügen Sie den Namen am Ende der Liste an 
  und geben Sie die neue Liste aus.
- Jedes Mal, wenn die Eingabe bereits in der Liste auftaucht, verkürzen Sie die Liste so, dass alle Listeneinträge
  ab dem ersten Auftreten der Eingabe aus der Liste entfernt werden.
  Ist die Liste wieder leer, beenden Sie das Programm und verabschieden Sie den Benutzer, 
  ansonsten geben Sie die neue Liste aus.

Beispiel: Starte mit leerer Liste []
- Eingabe "Bruno" -> Ausgabe: ["Bruno"]
- Eingabe "Heidi" -> Ausgabe: ["Bruno", "Heidi"]
- Eingabe "Kurt"  -> Ausgabe: ["Bruno", "Heidi", "Kurt"]
- Eingabe "Lara"  -> Ausgabe: ["Bruno", "Heidi", "Kurt", "Lara"]
- Eingabe "Kurt"  -> Ausgabe: ["Bruno", "Heidi"]
- Eingabe "Bruno" -> Ausgabe: "Ciao!"

"""

li = []

while True:
    name = input("Geben Sie bitte einen Namen ein: ")
    if name in li:
        li = li[: li.index(name)]
        if li == []:
            break
    else:
        li.append(name)
    print(li)

print("Ciao!")
