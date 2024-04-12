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

class Entity:

     dir_dict = {"Up": (0,-1), "Down": (0,1), "Left": (-1,0), "Right": (1,0)}

     def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        
     def can_move(self, playground):
        dx, dy = self.dir_dict[self.dir]
        new_x = self.x + dx
        new_y = self.y + dy
        max_x, max_y = playground.shape
        return 0 <= new_x < max_x and 0 <= new_y < max_y and playground[new_x][new_y] != 1


if __name__ == '__main__':
    import numpy as np
    entity = Entity(2,2, "Right")
    playground = np.array([[1, 0, 0, 1, 0, 1],
                           [1, 0, 0, 0, 0, 1],
                           [0, 0, 0, 1, 0, 0],
                           [1, 0, 0, 0, 0, 1]]
                         ).T
    print(entity.can_move(playground))
