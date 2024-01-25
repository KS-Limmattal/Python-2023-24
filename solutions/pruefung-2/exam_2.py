#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Prüfungsaufgabe 2 (vom 19.1.2024)

Ersetzen Sie in den folgenden Funktionen den behelfsmässigen 'pass' Befehl mit den passenden Anweisungen.
"""


def is_perfect(n: int):
    """
    Überprüft, ob eine natürliche Zahl perfekt ist, d.h. mit der Summe ihrer echten Teiler
    übereinstimmt.
    z.B. sind 6, 28 und 496 perfekt (6 = 1+2+3, 28=1+2+4+7+14, 496 = 1+2+4+8+16+31+62+124+248).

    :param n: die natürliche Zahl
    :return: True, falls perfekt; False sonst
    """
    return sum([t for t in range(1, n) if n % t == 0]) == n


def value_count(orig_dict):
    """
    Liefert für ein Wörterbuch, dessen Werte Listen von ganzen Zahlen sind, ein neues
    Wörterbuch zu, welches jeder der in wenigstens einer Liste auftauchenden Zahlen die Zahl zuordnet,
    welche angibt, wie oft die Zahl insgesamt in den Listen vorkommt.
    Bsp: value_count({"a":[1,3,5], "b":[2,5], "c":[1,2,1,5]}) == {1: 3, 2: 2, 3: 1, 5: 3},
         denn die 1 kommt 3 Mal vor (1 Mal in der Liste für "a", zweimal in der für "c"),
              die 2 kommt 2 Mal vor,
              die 3 kommt 1 Mal vor,
              die 5 kommt 3 Mal vor.

    :param orig_dict: Das Wörterbuch, deren Werte Listen von ganzen Zahlen sind
    :return: Das Wörterbuch, welches die Vorkommnisse zählt
    """
    return_dict = {}
    for val_list in orig_dict.values():
        for val in val_list:
            if val in return_dict:
                return_dict[val] += 1
            else:
                return_dict[val] = 1

    return return_dict
