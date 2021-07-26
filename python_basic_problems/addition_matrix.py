# Python Program to Add Two Matrices

import numpy as np

matrix_1 = np.matrix([[1, 2, 3], [4, 5, 6]])
matrix_2 = np.matrix([[4, 5, 3], [7, 6, 9]])
matrix_result = np.add(matrix_1, matrix_2)
print(matrix_result)
