#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return (None)
    return list(list(map(lambda x: x*x, num_list)) for num_list in matrix)
