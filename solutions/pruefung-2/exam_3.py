#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Prüfungsaufgabe 3 (vom 19.1.2024)

Ersetzen Sie in den folgenden Funktionen den behelfsmässigen 'pass' Befehl mit den
passenden Anweisungen und geben Sie danach mit Hilfe der Funktion
closest_number die Zahl der Liste [1.3, 5.2, 3.6, 4.2, 8.75] mit kleinstem Abstand zur Zahl 2.7
in einem sauber formatierten Satz aus.
"""


def closest_number(li, num):
    """
    Liefert für eine Liste li von Zahlen und eine vorgegebene Zahl num die Zahl der Liste li
    zurück, welche den kleinsten Abstand von num hat. Ist diese Zahl nicht eindeutig,
    so soll die letzte Zahl der Liste mit kleinstem Abstand zu num zurückgegeben werden

    :param li: Die Liste von Zahlen (floats, int sind beides erlaubt)
    :param num: Die Zahl, zu der der Abstand kleinstmöglich sein soll
    :return: Die (letzte) Zahl der Liste mit kleinstem Abstand
    """

    ret = li[0]
    d = abs(ret - num)
    for k in li[1:]:
        d_new = abs(k - num)
        if d_new <= d:
            ret = k
            d = d_new

    return ret


"""
def continued_fraction_recursive(li):
    if len(li)==1:
        return li[0]
    else:
        return li[0] + 1 / continued_fraction(li[1:])
"""


def continued_fraction(li):
    """
    Liefert für eine Liste von positiven Zahlen [a_0, a_1, a_2, ..., a_n] den entsprechenden
    Kettenbruch definiert als a_0 + 1/(a_1 + 1/(a_2 + 1/(a_3 + ...))) zu

    :param li: Die Liste der positiven Zahlen
    :return: Der Kettenbruch
    """

    ret = li[-1]
    for i in range(2, len(li) + 1):
        ret = li[-i] + 1 / ret
    return ret


if __name__ == "__main__":
    # Hier gehört der Funktionsaufruf hin (statt `pass`)
    li = [1.3, 5.2, 3.6, 4.2, 8.75]
    num = 2.7
    print(
        f"Die Zahl der Liste {li}, die am nächsten zu {num} liegt, lautet {closest_number(li, num)}"
    )
