#!/usr/bin/python3
"""A module that rotates an n x n matrix by 90 degs"""

def rotate_2d_matrix(matrix):
    """
        A function that edits in-place a rotated matrix by 90 degs
    """
    n = len(matrix[0])

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
