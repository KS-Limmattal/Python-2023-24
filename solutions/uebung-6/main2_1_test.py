#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from main2 import erstesR

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""


def test():
    assert erstesR(["Roland", "Stefan", "Klara", "Ritalin", "Hans"]) == "Roland"
    assert erstesR(["Otto", "Stefan", "Klara"]) == "Klara"
    assert erstesR(["Wochentag", "Suppe", "stehen", "Wille", "Kino"]) == ""
    assert erstesR(["Michael", "Kurt", "Rebekka"]) == "Kurt"
    assert erstesR([]) == ""
