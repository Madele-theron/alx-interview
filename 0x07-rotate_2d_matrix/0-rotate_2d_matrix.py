#!/usr/bin/python3
"""Module to rotate a 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix in place, no return statement"""
    left = 0
    right = len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top = left
            bottom = right

            temp = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = temp

        right -= 1
        left += 1
