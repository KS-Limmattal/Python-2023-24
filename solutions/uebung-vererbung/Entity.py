#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Klasse "Entity" mit

- Eigenschaften: x, y, (für Position)
                 dir   (Richtung: "Up", "Down", "Left" oder "Right")

- Methoden:  - __init__ (Konstruktor)
             - can_move:  mit Argument playground, welches ein numpy array bestehend aus Nullen (frei) und Einsen (Wand) ist
	       Diese Methode überprüft, ob sich die Entität in gegebener Richtung bewegen kann
               Bsp: Ist self.x == 4, self.y == 7, self.dir = "Up" und playground[4][6] == 0,
                    so muss der Rückgabewert True sein, da mit "Up" das freie Feld mit Koordinaten (4, 6) erreicht würde.
               Hinweis: Auch die Grösse des Spielfelds ist zu beachten. Die Entität kann nicht über den Spielfeldrand hinausfahren.
"""
