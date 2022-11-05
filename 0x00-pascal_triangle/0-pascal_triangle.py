#!/usr/bin/python3
"""
function def pascal_triangle(n)
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    # case 1: n less than 0
    if n <= 0:
        return []
    # case 2: n equal to 1
    if n == 1:
        return [[1]]
    triangle = [[1]]
    # case 3: n greater than 1
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle