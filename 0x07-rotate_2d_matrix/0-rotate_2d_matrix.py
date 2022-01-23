#!/usr/bin/python3
'''
Python3 program to rotate a square matrix by 90 degree
'''


def rotate_2d_matrix(matrix):
	''' rotate 2D matrix by 90 degrees
	Args:
		matrix (list[[list]]): a matrix
	'''
	n = len(matrix)
	for i in range(int(n / 2)):
		y = (n - i - 1)
		for j in range(i, y):
			x = (n - 1 - j)
			# current number
			tmp = matrix[i][j]
			# change top for left
			matrix[i][j] = matrix[x][i]
			# change left for bottom
			matrix[x][i] = matrix[y][x]
			# change bottom for right
			matrix[y][x] = matrix[j][y]
			# change right for top
			matrix[j][y] = tmp
