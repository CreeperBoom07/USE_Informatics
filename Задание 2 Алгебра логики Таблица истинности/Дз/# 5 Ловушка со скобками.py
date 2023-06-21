"""Всегда следить за приоритетом в лог. выражении"""
from itertools import product as pd, permutations as pm


def f(x, y, z, w):
    return (x <= (y and 1-z)) or w


for x in pd([0, 1], repeat=6):

    matrix = [(x[0], x[1], 1, 0),
              (0, x[2], x[3], 1),
              (1, x[4], 1, x[5])]

    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
                print(*p, sep='')
