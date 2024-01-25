#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Finden und korrigieren Sie den Fehler im folgenden Programmtext.
"""


def is_square_free(n: int):
    """
    Überprüft, ob eine gegebene Zahl quadratfrei ist,
    also keinen Teiler > 1 hat, dessen Quadrat die Zahl ebenfalls teilt

    :param n: Die gegebene Zahl
    :return: True, falls quadratfrei; False, false nicht quadratfrei
    """
    for t in range(2, n):
        if n % t == 0 and n % t**2 == 0:
            return False

    return True  # Erst, wenn alle Teiler geprüft sind, kann diese Rückgabe erfolgen


for n in [10, 100, 12, 1, 99]:
    print(f"Ist n = {n} quadratfrei? {is_square_free(n)}")
