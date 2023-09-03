#!/usr/bin/python3
"""a function def island_perimeter(grid): that returns the
perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Takes an argument grid and returns the parameter
    """
    island_pm = 0
    if isinstance(grid, list) == False:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                island_pm += 4
                if i > 0 and grid[i-1][j] == 1:
                    island_pm -= 2
                if j > 0 and grid[i][j-1] == 1:
                    island_pm -= 2
    return island_pm
