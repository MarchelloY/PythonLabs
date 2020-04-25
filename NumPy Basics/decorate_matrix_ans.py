import numpy as np
import sys

MATRIX_BORDER_NUMBER = 1

def fill_the_borders_of_the_matrix(matrix, border_number):
    matrix[0] = border_number
    matrix[-1] = border_number
    matrix[:, 0] = border_number
    matrix[:, -1] = border_number

def decorate_matrix(matrix_dimension):
    matrix = np.zeros((matrix_dimension, matrix_dimension), dtype='int')
    fill_the_borders_of_the_matrix(matrix, MATRIX_BORDER_NUMBER)
 
    return matrix

matrix_dimension = sys.argv[1]
matrix = decorate_matrix(int(matrix_dimension))
print(matrix)