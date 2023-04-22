#!/usr/bin/python3
"""
Pascals triangle of n method:
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascals triangle
    """
    if n <= 0:

        return []
    else:
        triangle = []

        for row in range(n):
            # this will determine the number of columns in each row:
            next_row = [1] * (row + 1)
            for col in range(1, row):
                next_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
            triangle.append(next_row)

        return triangle
