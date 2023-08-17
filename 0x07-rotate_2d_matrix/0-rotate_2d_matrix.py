#!/usr/bin/python3
"""Rotate 2D Matrix"""

def rotate_2d_matrix(matrix):
    """Matrix"""
    row = len(matrix)
    columns = len(matrix[0]) if row > 0 else 0

    trans = [[0 for _ in range(row)] for _ in range(columns)]

    for i in range(row):
        for j in range(columns):
            trans[j][i] = matrix[i][j]

    return trans
