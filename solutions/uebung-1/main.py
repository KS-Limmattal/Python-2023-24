#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def gruesse(vorname: str):
    """
    @param vorname    Ein Vorname
    @return           Eine Grussformel der Form "Hallo ...", wobei ... für den Vornamen steht, bzw.
                      "Ach, dieser Name ist mir zu lang!", falls der Vorname aus mehr als 6 Buchstaben besteht
    """
    if len(vorname) <= 6:
        return f"Hallo {vorname}"

    return "Ach, dieser Name ist mir zu lang!"


def mehrfach(vorname: str):
    """
    @param vorname    Ein Vorname
    @return           True, falls der Name einen Buchstaben mehrfach enthält, False sonst.
                      Dabei wird nicht zwischen Klein- und Grossbuchstaben unterschieden.
    """

    vorname_klein = vorname.lower()
    for letter in vorname_klein:
        if vorname_klein.count(letter) > 1:
            return True

    return False


if __name__ == "__main__":
    # Dieser Code wird ausgeführt, wenn das Programm gestartet wird (zum eigenständigen Testen)
    print(gruesse("Hans"))
    print(gruesse("Sebastian"))
    print(mehrfach("Hans"))
    print(mehrfach("Susanne"))
