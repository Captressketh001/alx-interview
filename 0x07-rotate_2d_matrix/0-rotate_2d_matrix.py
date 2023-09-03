#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Matrix"""
    z = zip(*reversed(matrix))
    for x, y in enumerate(z):
        matrix[x] = list(y)
