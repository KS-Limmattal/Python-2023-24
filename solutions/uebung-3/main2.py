#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Schreiben Sie ein Programm, welches zu einer (nicht unbedingt invertierbaren) gegebenen Matrix die 
Adjunkte (gebildet durch Determinanten von Streichmatrizen) berechnet
Überprüfen Sie Ihr Ergebnis, indem Sie die Adjunkte mit der ursprünglichen Matrix multiplizieren

Bsp: A = np.array( [ [1.,2.,3.] , [4.,5.,6.] , [7.,8.,9.] ] )              (vorgegeben)
    Adj = np.array( [ [-3., 6., -3.], [6., -12., 6.], [-3., 6., -3.] ] )   (berechnet)
"""


import numpy as np

A = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])

n = A.shape[0]  # Anzahl Zeilen, sollte mit Anzahl Spalten übereinstimmen

Adj = np.zeros(A.shape)

for i in range(n):
    for j in range(n):
        streichmatrix = np.zeros((n - 1, n - 1))
        streichmatrix[:i, :j] = A[:i, :j]  # links oben
        streichmatrix[i:, :j] = A[i + 1 :, :j]  # links unten
        streichmatrix[:i, j:] = A[:i, j + 1 :]  # rechts oben
        streichmatrix[i:, j:] = A[i + 1 :, j + 1 :]  # rechts unten
        Adj[j, i] = (-1) ** (i + j) * np.linalg.det(streichmatrix)

print(f"Die Adjunkte der Matrix \n {A} \n lautet \n {Adj}")
