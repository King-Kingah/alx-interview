#!/usr/bin/python3
'''
Python3 program to rotate a square matrix by 90 degree
'''


def rotate_2d_matrix(matrix):
    '''
    rotate 2d matrix by 90 degree
    Args:
    matrix (list[[list]]): a matrix
    '''
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            # the number
            temp = matrix[i][j]
            # top for left
            matrix[i][j] = matrix[x][i]
            # left for bottom
            matrix[x][i] = matrix[y][x]
            # bottom for right
            matrix[y][x] = matrix[j][y]
            # right for top
            matrix[j][y] = temp
