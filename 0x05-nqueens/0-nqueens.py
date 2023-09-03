#!/usr/bin/python3
"""he N queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard. Write a program that solves the N queens problem.
"""
import sys


def print_board(board, n):
    """print_board allocated to the queen"""
    b = []

    for x in range(n):
        for y in range(n):
            if y == board[x]:
                b.append([x, y])
    print(b)


def safe_position(board, i, j, r):
    """Safe_position for the queen"""
    return board[i] in (j, j - i + r, i - r + j)


def determine_positions(board, row, n):
    """determine_positions where the queen can be allocated"""
    if row == n:
        print_board(board, n)

    else:
        for j in range(n):
            allowed = True
            for i in range(row):
                if safe_position(board, i, j, row):
                    allowed = False
            if allowed:
                board[row] = j
                determine_positions(board, row + 1, n)


def create_board(size):
    """Generates the board"""
    return [0 * size for i in range(size)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

board = create_board(int(n))
row = 0
determine_positions(board, row, int(n))
