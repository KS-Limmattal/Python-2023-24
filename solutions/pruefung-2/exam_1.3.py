#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Finden und korrigieren Sie den Fehler im folgenden Programmtext.
"""


def reverse_list(li):
    """
    Gibt eine Liste zurück, welche die gleichen Elemente wie die originale Liste,
    aber in umgekehrter Reihenfolge, enthält.
    :param li: Die Liste
    :return: Die umgekehrte Liste
    """

    rev_list = []
    for i in range(len(li) - 1, -1, -1):
        rev_list.append(li[i])  # Eckige Klammern statt runde Klammern

    return rev_list


print(reverse_list([3, 1, 4, 1, 5, 9, 2, 6]))
