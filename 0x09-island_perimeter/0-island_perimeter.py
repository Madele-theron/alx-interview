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
    
    row = len(grid)
    column = len(grid[0])
    assert (1 <= row and column <= 100), "length must be between 1 an 100"

    perimeter_total = 0
    
    # search for 1's
    for i in range(row):
        for j in range(column):
            if j == 1:
                perimeter_total += count_perimeter(grid, i, j)
    return perimeter_total - 1


def count_perimeter(grid, row, column):
    """increase the counter if it's a 0 or out of bound

    Args:
        grid (list): the grid
        row (list):the row of the grid
        column (int):the column of the grid
    """
    counter = 0
    # top
    if row + 1 >= len(grid) or grid[row + 1][column] == 0:
        counter += 1
    # right
    if column + 1 >= len(grid) or grid[row][column + 1] == 0:
        counter += 1
    # bottom
    if row - 1 < 0 or grid[row -1][column] == 0:
        counter += 1
    # left
    if column - 1 < 0 or grid[row][column - 1] == 0:
        counter += 1
    return counter



grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
print(island_perimeter(grid))