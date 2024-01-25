#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Prüfungsaufgabe 4 (vom 19.1.2024)

Bei dieser Aufgabe liegt ein funktionierendes Programm vor. Das Programm ist nicht optimal geschrieben, 
da sich Code-Teile mehrfach in fast identischer Form wiederholen. Es soll so umgeschrieben werden, 
dass die wiederholenden Teile in zwei neu zu verfassende Funktionen ausgelagert werden, welche dann nur
mit verschiedenen Parameterwerten aufgerufen werden brauchen.
"""

from math import sqrt

r = 10


def input_circle(name):
    x1 = float(input(f"Geben Sie die x-Koordinate des Mittelpunkts von {name} ein: "))
    y1 = float(input(f"Geben Sie die y-Koordinate des Mittelpunkts von {name} ein: "))
    print(f"Die Gleichung von {name} lautet (x-{x1})^2 + (y-{y1})^2 = {r**2}")
    return x1, y1


def compute_intersection(x1, y1, name1, x2, y2, name2):
    d12_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
    D12 = r**2 / d12_squared - 1 / 4
    if D12 > 0:
        t12 = sqrt(D12)
        x12_1 = (x1 + x2) / 2 + t12 * (y2 - y1)
        y12_1 = (y1 + y2) / 2 + t12 * (x1 - x2)
        x12_2 = (x1 + x2) / 2 - t12 * (y2 - y1)
        y12_2 = (y1 + y2) / 2 - t12 * (x1 - x2)
        print(
            f"Die Schnittpunkte von {name1} und {name2} lauten ({x12_1}, {y12_1}) sowie ({x12_2}, {y12_2})"
        )
    elif D12 == 0:
        x12 = (x1 + x2) / 2
        y12 = (y1 + y2) / 2
        print(f"Der einzige Schnittpunkt von {name1} und {name2} lautet {x12, y12}")
    else:
        print(f"Die Kreise {name1} und {name2} schneiden sich nicht")


print(f"Geben Sie im Folgenden die Mittelpunkte dreier Kreise von Radius {r} ein")

x1, y1 = input_circle("k1")
x2, y2 = input_circle("k2")
x3, y3 = input_circle("k3")

compute_intersection(x1, y1, "k1", x2, y2, "k2")
compute_intersection(x1, y1, "k1", x3, y3, "k3")
compute_intersection(x2, y2, "k2", x3, y3, "k3")
