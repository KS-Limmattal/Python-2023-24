#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from main2 import streicheVerdoppelte

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""


def test():
    li1 = ["doppelt", "Aare", "Ananas", "Stein"]
    streicheVerdoppelte(li1)
    assert li1 == ["Aare", "Ananas", "Stein"]

    li2 = ["Anna", "Stefan", "Klara", "Betti"]
    streicheVerdoppelte(li2)
    assert li2 == ["Stefan", "Klara"]

    li3 = ["Wochentag", "Suppe", "stehen", "Wille", "Kino"]
    streicheVerdoppelte(li3)
    assert li3 == ["Wochentag", "stehen", "Kino"]

    li4 = ["Michael", "Kurt", "Rebekka"]
    streicheVerdoppelte(li4)
    assert li4 == ["Michael", "Kurt"]

    li5 = []
    streicheVerdoppelte(li5)
    assert li5 == []

    li6 = ["keine", "verdopPelung", "haha", "Aua", "Aare"]
    streicheVerdoppelte(li6)
    assert li6 == ["keine", "verdopPelung", "haha", "Aua", "Aare"]

    li7 = ["Aha", "Glosse", "Karikatur"]
    streicheVerdoppelte(li7)
    assert li7 == ["Aha", "Karikatur"]

    li8 = ["Aha", "Gloria", "Karikatur"]
    streicheVerdoppelte(li8)
    assert li8 == ["Aha", "Gloria", "Karikatur"]
    
    li9 = ["doppelt", "alles", "verdoppelt"]
    streicheVerdoppelte(li9)
    assert li9 == []

