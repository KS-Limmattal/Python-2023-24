#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functions import f

"""
Für Funktionen können automatisierte Tests geschrieben werden, welche
die Richtigkeit der Funktionsimplementierung testen und bei Überarbeitung
der Funktion vor Rückschritten schützt

Die Tests werden mit Hilfe des Befehls `pytest` ausgeführt; letzteres
sucht nach allen Dateien mit Namen `test_*.py`, führt alle darin
enthaltenen Tests (Funktionen mit Namen test_*`) aus und meldet bestandene
und nicht bestandene Tests
"""


def test_f():
    assert f(0) == 1
    assert f(2) == 11


"""
Ein `assert` ist eine Behauptung der Richtigkeit einer Bedingung
Üblicherweise steht links der Aufruf der zu testenden Funktion und
rechts der von der Programmierer:in vorgesehenen Funktionswert
"""
