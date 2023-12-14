#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from main1 import anzahlPaare

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""


def test():
    assert anzahlPaare(2) == 1
    assert anzahlPaare(3) == 3
    assert anzahlPaare(10) == 45
    assert anzahlPaare(20) == 190
