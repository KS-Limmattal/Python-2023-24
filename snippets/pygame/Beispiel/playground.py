# -*- coding: utf-8 -*-
import pygame
import numpy as np
from enum import IntEnum

WINDOW_WIDTH, WINDOW_HEIGHT = 1600, 1000
MARGIN = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Stein(IntEnum):
    FIRST = -1
    EMPTY = 0
    SECOND = 1


class Playground:

    def __init__(self, num_rows, num_cols, size):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.size = size
        self.offset_x = MARGIN
        self.offset_y = WINDOW_HEIGHT - self.num_rows * self.size - MARGIN
        self.radius = int(0.4*size)
        self.mat = np.zeros((num_rows, num_cols), dtype=Stein)

    def is_full(self, col):
        return np.all(self.mat.T[col] != Stein.EMPTY)

    def add(self, col, stein):
        assert not self.is_full(col)
        assert not stein == Stein.EMPTY
        first = np.argmax(self.mat.T[col] != Stein.EMPTY)
        self.mat[first - 1][col] = stein

    def is_valid(self, col, row):
        return 0 <= col < self.num_cols and 0 <= row < self.num_rows

    def check_finish(self):
        dir_list = {
            "up": np.array([0, 1]),
            "right": np.array([1, 0]),
            "right up": np.array([1, 1]),
            "left up": np.array([1, -1]),
        }
        for dr, dc in dir_list.values():
            for row in range(self.num_rows):
                for col in range(self.num_cols):
                    if self.is_valid(col + 3 * dc, row + 3 * dr):
                        indices = [(row + dr * i, col + dc * i) for i in range(4)]
                        if sum([self.mat[c, r] for c, r in indices]) in [
                            4 * Stein.FIRST,
                            4 * Stein.SECOND,
                        ]:
                            return indices

        return []
    
    def __str__(self):
        return " "+f"{self.mat + 0}".replace("0","-").replace("-1","+").replace("1","*")[1:-1]+"\n"

    def draw(self, surface):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = (col+.5) * self.size + self.offset_x
                y = (row+.5) * self.size + self.offset_y
                stein = self.mat[row, col]
                if stein == Stein.FIRST:
                    pygame.draw.circle(surface, BLUE, (x, y), self.radius)
                elif stein == Stein.SECOND:
                    pygame.draw.circle(surface, RED, (x, y), self.radius)

    def highlight(self, surface, indices):
        for r, c in indices:
            rect = pygame.Rect(
                c * self.size + self.offset_x,
                 r * self.size + self.offset_y,
                self.size,
                self.size,
            )
            pygame.draw.rect(surface, BLACK, rect, width=2)
