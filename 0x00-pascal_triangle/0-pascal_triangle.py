#!/usr/bin/python3
'''
function def pascal_triangle(n)
'''

def pascal_triangle(n):
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



''' Second approach using built-in function: factorial'''
# from math import factorial
#
# # where n is the number of rows
# def pascal_triangle(n):
#     for i in range(n):
#         # first loop for leading spaces
#         for j in range(n - i + 1):
#             print(end = " ")
#
#         # second loop for row i elements
#         for j in range(i + 1):
#             # define factorial formula: nCr = n!/((n-r)!*r!)
#             print(factorial(i)//(factorial(j)*factorial(i - j)), end = " ")
#
#         # print each row in a new line
#         print("\n")