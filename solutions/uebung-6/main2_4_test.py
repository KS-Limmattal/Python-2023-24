#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from main2 import palindrome

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""


def test():
    assert palindrome(["Aha", "Echo", "Anna", "Rentner", "gaga"]) == [
        "Aha",
        "Anna",
        "Rentner",
    ]
    assert palindrome(["Palindrom", "haiah"]) == ["haiah"]
    assert palindrome(["Hier", "gibt", "es", "kein", "Palindrom"]) == []
    assert palindrome([]) == []
