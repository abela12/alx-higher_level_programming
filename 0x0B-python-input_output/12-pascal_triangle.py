#!/usr/bin/python3
""" pascal triangle"""


def pascal_triangle(n=4500):
    """print pascal"""
    pascal = [[0]*i for i in range(1, n+1)]
    cmpt = 0
    for i in range(n):
        pascal[i][0] = 1
        pascal[i][-1] = 1
        for j in range(0, i//2):
            pascal[i][j+1] = pascal[i-1][j] + pascal[i-1][j+1]
            pascal[i][i-j-1] = pascal[i-1][j] + pascal[i-1][j+1]

    return pascal
