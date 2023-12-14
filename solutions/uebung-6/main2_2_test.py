#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from main2 import letzteVerdopplung

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""


def test():
    assert letzteVerdopplung(["doppelt", "Aare", "Ananas", "Stein"]) == "doppelt"
    assert letzteVerdopplung(["Anna", "Stefan", "Klara", "Betti"]) == "Betti"
    assert letzteVerdopplung(["Woche", "Suppe", "stehen", "Wille", "Kino"]) == "Wille"
    assert letzteVerdopplung(["Michael", "Kurt", "Rebekka"]) == "Rebekka"
    assert letzteVerdopplung([]) == ""
    assert letzteVerdopplung(["keine", "verdopPelung", "haha", "Aua", "Aare"]) == ""

    li1 = ["Aha", "Glosse", "Karikatur"]
    li1Copy = li1.copy()
    ret1 = letzteVerdopplung(li1)
    assert ret1 == "Glosse"
    assert li1 == li1Copy

    li2 = ["Aha", "Gloria", "Karikatur"]
    li2Copy = li2.copy()
    ret2 = letzteVerdopplung(li2)
    assert ret2 == ""
    assert li2 == li2Copy
