#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    col_len = len(matrix[0])
    for row in range(len(matrix)):
        for column in range(col_len):
            if column == col_len - 1:
                print("{:d}".format(matrix[row][column]), end="")
                break
            print("{:d}".format(matrix[row][column]), end=" ")
        print()
