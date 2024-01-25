#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Finden und korrigieren Sie den Fehler im folgenden Programmtext.
"""


def contains_multiple_elements(li):
    """
    Gibt zurück, ob die gegebene Liste mindestens ein Element mehrfach enthält
    :param li: Die Liste
    :return: True, falls ein Element mehrfach enthalten ist, False sonst.
    """
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] == li[j]:  # Vergleich, nicht Zuweisung
                return True

    return False
