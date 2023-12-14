#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from main1 import wurzelApprox
import numpy as np

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""


def test():
    assert np.isclose(wurzelApprox(4, 0.001), 2, atol=0.001)
    assert np.isclose(wurzelApprox(2,0.0001), 1.41421, atol=0.0001)
    assert np.isclose(wurzelApprox(9, 0.00001), 3, atol=0.00001)
    assert np.isclose(wurzelApprox(4.35, 0.000001), 2.085665361, atol=0.000001)
