#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Erstellen Sie ein Wörterbuch (dictionary), welches dem Kürzel jeder Fachlehrperson der Klasse M5a den vollen Namen zuordnet
(z.B. 'loe' wird zu 'Roland Lötscher')
Erzeugen Sie danach daraus eine Liste aller Kürzel der Namen der Fachlehrpersonen, welche einen Umlaut enthalten.
"""

name = {
    "loe": "Roland Lötscher",
    "flu": "Livia Flury",
    "bas": "Caren Bastian",
    "rus": "Nicola Rusca",
    "mie": "Samuel Miesch",
    "dmo": "Raphael De Moliner",
    "mul": "Paul Muller",
    "gro": "Corinne Grossert",
    "wen": "Ingrid Wenk-Siefert",
    "bun": "Marc Bundi",
    "leh": "Martin Lehmann",
    "ger": "Esther Gersbach",
    "rob": "Elena Robbiani",
    "tmb": "Sandra Tamburro",
}

list = [k for k in name.keys() if "ö" in name[k] or "ü" in name[k] or "ä" in name[k]]
