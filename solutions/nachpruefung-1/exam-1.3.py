#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nachprüfung Aufgabe 3 (vom 1.12.2023)

Lassen Sie den Benutzer wiederholt (erwachsene) Personen durch die Angabe von 
 
 - "Name",
 - "Vorname",
 - "Adresse" und
 - "Alter" (Ganzzahl) 

eingeben.
Ist jeweils das Alter der Person grösser als 60 Jahre, lassen Sie den Benutzer auch die Frage beantworten,
ob die Person pensioniert ist. Ist das Alter kleiner als 60 Jahre oder die Person nicht pensioniert, 
so fragen Sie auch den Arbeitsort der Person ab. Brechen Sie das Programm ab, wenn der Name leer ist
(d.h. es wird direkt die Enter-Taste gedrückt).
"""

while True:
    print("Geben Sie für eine Person folgende Angaben ein.")
    name = input("Name: ")
    if name == "":
        break
    vorname = input("Vorname: ")
    adresse = input("Adresse: ")
    alter = int(input("Alter: "))
    if alter > 60:
        pensioniert = input("Pensioniert (j/n): ")

    if alter < 60 or pensioniert == "n":
        arbeitsort = input("Arbeitsort: ")

