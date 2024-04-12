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

from Entity import Entity
class Pacman(Entity):
    point_dict = {"Point": 10, "Fruit": 100, "Pill": 200}

    def __init__(self, lives, score, can_eat_ghost):
        super().__init__(0, 0, "Right")
        self.lives = lives
        self.score = score
        self.can_eat_ghost = can_eat_ghost

    def dec_lives(self):
        if self.lives > 0:
            self.lives -= 1
        else:
            print("Game over")

    def inc_score(self, s):
        self.score += self.point_dict[s]

if __name__ == '__main__':
    pacman = Pacman(3, 0, False)
    pacman.inc_score("Point")
    pacman.dec_lives()
    print(f"lives: {pacman.lives}, score: {pacman.score}")
