#!/usr/bin/python3
"""island perimeter interview question
"""


def island_perimeter(grid):
    """Algorithm for determining the perimeter of an island grid

    Args:
        grid list: the list of 0s and 1s
        that represent water (0) or island (1)
    """
    if grid is None:
        return 0

    perimeter_total = 0
    # step 1
    for i in range(len(grid)):
        print("i", i)
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter_total += count_perimeter(grid, i, j)
    return perimeter_total


def count_perimeter(grid, i, j):
    """increase the counter if it's a 0 or out of bound

    Args:
        grid (list): the grid
        row (list):the row of the grid
        column (int):the column of the grid
    """
    count = 0
    if j - 1 < 0 or grid[i][j - 1] == 0:
        count += 1
    if j + 1 >= len(grid[0]) or grid[i][j + 1] == 0:
        count += 1
    if i - 1 < 0 or grid[i - 1][j] == 0:
        count += 1
    if i + 1 >= len(grid) or grid[i + 1][j] == 0:
        count += 1
    return count
