#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat_cpy = list()
    for row in matrix:
        mat_cpy_row = list()
        for i in row:
            mat_cpy_row.append(i**2)
        mat_cpy.append(mat_cpy_row)
    return mat_cpy
