#!/usr/bin/python3
"""
This module contains a function that generates Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): The number of rows of the triangle to generate.

    Returns:
        list: A list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        prev_row = triangle[-1]
        # Every row starts with 1
        new_row = [1]

        # Calculate middle elements by summing adjacent elements in prev_row
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])

        # Every row ends with 1
        new_row.append(1)
        triangle.append(new_row)

    return triangle
