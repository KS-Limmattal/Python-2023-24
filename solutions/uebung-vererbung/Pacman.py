#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Klasse "Pacman" mit Basisklasse "Entity" und zusätzlichen

- Eigenschaften: lives         (verbliebene Leben)
                 score         (Punktezahl)
                 can_eat_ghost (ob Pacman gerade eine Pille Intus hat)

- Methoden:      dec_lives (vermindert Lebenszahl, falls > 0; Ausgabe "Game over" andernfalls)
                 inc_score (nimmt eine Zeichenkette s als Argument und erhöht die Punktezahl um
                           10 Punkte, falls  s == "Point"
                           100 Punkte, falls s == "Fruit"
                           200 Punkte, falls s == "Pill"
"""
