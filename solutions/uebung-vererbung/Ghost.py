#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Klasse "Ghost" mit Basisklasse "Entity" und zusätzlichen

- Eigenschaften: home_x      (x-Koordinate des Ausgangsfelds)
                 home_y      (y-Koordinate des Ausgangsfelds)

- Methoden:      choose_dir: gibt eine zufällige Richtung "Up", "Down", "Left" oder "Right" zurück
                 distance:   berechnet die geometrische Distanz, welche den Geist aktuell von seinem Ausgangsfeld trennt
"""
from Entity import Entity
import random
import math

class Ghost(Entity):
    def __init__(self, home_x, home_y):
        super().__init__(0, 0, "Right")
        self.home_x = home_x
        self.home_y = home_y

    def choose_dir(self):
        return random.choice(["Up", "Down", "Left", "Right"])

    def distance(self):
        return math.sqrt((self.home_x - self.x)**2 + (self.home_y - self.y)**2)

if __name__ == '__main__':
    ghost = Ghost(2, 3)
    print(f"Random direction: {ghost.choose_dir()}")
    print(f"Distance from home: {ghost.distance()}")