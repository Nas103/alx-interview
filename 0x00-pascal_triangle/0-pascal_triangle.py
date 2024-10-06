#!/usr/bin/python3
"""
0-pascal_triangle module
This module contains the function pascal_triangle(n) that returns
a list of lists of integers representing Pascal's Triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n

    Args:
        n (int): Number of rows in Pascal's triangle

    Returns:
        list: A list of lists representing Pascal's Triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Starting row

    for i in range(1, n):
        row = [1]  # Each row starts with 1
        prev_row = triangle[i - 1]

        # Create the middle values
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # Each row ends with 1
        triangle.append(row)

    return triangle
