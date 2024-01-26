#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eine Klasse ist ein Bauplan für Objekte eines bestimmten Typs.
Eine Instanz einer Klasse ist eine Realisierung dieses Bauplans.

Klassen haben 
- Eigenschaften: Variablen, welche alle Instanzen derselben Klasse haben
- Methoden: Funktionen, welche alle Instanzen derselben Klasse haben, und welche eine Zustandsänderung einer Instanz ermöglichen
            Jede Methode der Klasse muss als erstes Argument "self" haben. Mit diesem Wort lässt sich auf die Eigenschaften einer
            Instanz zugreifen. Beim Aufruf muss dieses erste Argument weggelassen werden, da es automatisch übergeben wird

Eine Klasse (Bauplan) muss zuerst definiert werden, bevor Instanzen der Klasse angelegt werden können.
Bei der Instanzierung von Objekten wird die __init__ Methode der Klasse aufgerufen, um die Instanz zu konstruieren.

Der Vorteil von Klassen liegt darin, dass Variablen und Funktionen, die zum selben Typ von Objekt gehören, gebündelt werden können.
"""


class Person:
    """
    Diese Klasse realisiert einen Bauplan für eine Person
    Die Eigenschaften einer Person sollen der Vorname, Nachname, und das Alter (in Jahren) sein
    Die Methoden dieser Klasse sollen die Ausgabe des vollen Namens, eine Funktion zur Änderung des Nachnamens,
    sowie eine Funktion zur Inkrementierung (=Erhöhung um 1) des Alters sein.
    """

    def __init__(self, vorname, nachname, alter=0):
        """
        Konstruktor (konstruiert einen konkrete Person, also eine Instanz der Klasse)

        param vorname: der zugewiesene Vorname
        param nachname: der zugewiesene Nachname
        param alter: das zugewiesene Alter (standardmässig 0)
        """
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter

    def get_name(self):
        """
        return: der komplette Name der Person
        """
        return f"{self.vorname} {self.nachname}"

    def set_nachname(self, nachname):
        self.nachname = nachname

    def inkrementiere_alter(self):
        self.alter += 1


# Instanzierung von Personen (Objekten der Klasse Person) erfolgen nach der Definiton der Klasse

ex_praesident = Person("Donald", "Trump", 77)
baby = Person("Laura", "Müller")

# Nun können diese Instanzen, ihre Eigenschaften und Methoden verwendet werden

print(f"Ein amerikanischer Expräsident heisst {ex_praesident.get_name()}.")
ex_praesident.set_nachname("Trumpovski")
print(f"Der Expräsident heisst neu {ex_praesident.get_name()}.")
print(f"Aktuell ist das Baby {baby.alter} Jahre alt")
baby.inkrementiere_alter()
print(f"Nun ist das Baby {baby.alter} Jahre alt.")


""" 
Für Objekte wie Zahlen oder Zeichenketten gibt es Operatoren (wie +, * etc.) und Vergleichszeichen (wie ==, <= etc.)
Diese können auch für selber definierte Zahlen definiert werden. Dazu werden Funktionsnamen wie 
__add__  (für Addition)
__mul__ (für Multiplikation)
__eq__   (für Vergleich mit ==)
__le__   (für Vergleich mit <=)
verwendet.

Ein weiterer vorgegebener Methodenname ist auch __str__, welcher eine Zeichenketten-Darstellung des Objekts 
für Verwendung im print-Befehl zurückliefern soll.
"""


class Bruch:
    def __init__(self, zaehler, nenner):
        self.zaehler = zaehler
        self.nenner = nenner
        if self.nenner == 0:
            raise ValueError("0 darf nicht im Nenner stehen")

    def __eq__(self, other):
        return self.zaehler * other.nenner == self.nenner * other.zaehler

    def __mul__(self, other):
        return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)

    def __str__(self):
        return f"{self.zaehler}/{self.nenner}"


# Rechnen mit Brüchen (Instanzen der Klasse Bruch)

ein_halbes = Bruch(1, 2)
zwei_drittel = Bruch(2, 3)
produkt = ein_halbes * zwei_drittel
print(f"{ein_halbes} * {zwei_drittel} = {produkt}")
print(f"Ist das Produkt gleich 1/3? {produkt==Bruch(1,3)}")
print(f"Ist das Produkt gleich 5/7? {produkt==Bruch(5,7)}")
