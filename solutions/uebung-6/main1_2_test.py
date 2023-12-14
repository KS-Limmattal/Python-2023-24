#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from main1 import summeAbsEigval
import numpy as np

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""


def test():
    assert np.isclose(summeAbsEigval(np.array([[1.2, 0], [0, -3.5]])), 4.7)
    assert np.isclose(summeAbsEigval(np.array([[0, 1], [-1, 1]])), 2)
    assert np.isclose(summeAbsEigval(np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])), 3)
    assert np.isclose(summeAbsEigval(np.array([[1, 2], [3, 4]])), 5.744562646538029)
