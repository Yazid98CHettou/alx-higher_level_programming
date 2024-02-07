#!/usr/bin/python3
def pascal_triangle(n):
    """ Pascal Triangle 1h"""
    lis= []
    if n <= 0:
        return lis
    for r in range(n):
        for c in range(r + 1):
            if c == 0:
                lis.append([1])
            elif c == r:
                lis[r].append(1)
            else:
                lis[r].append(lis[r - 1][c] + lis[r - 1][c - 1])
    return lis
