#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_of_column = len(matrix[0])
    for row in range(len(matrix)):
        for column in range(len_of_column):
            if column == len_of_column - 1:
                print("{:d}".format(matrix[row][column]), end="")
                break
            print("{:d}".format(matrix[row][column]), end=" ")
        print()i
