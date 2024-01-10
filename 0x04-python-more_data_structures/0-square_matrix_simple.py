#!/usr/bin/bash
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x * x, a)) for a in matrix])
