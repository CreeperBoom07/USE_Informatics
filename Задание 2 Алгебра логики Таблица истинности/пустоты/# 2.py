from itertools import product as pd, \
    permutations as pm


def f(x, y, z, w):
    return (x == (not y)) <= ((x and w) == z)


def comb():
    for p in pm('xyzw'):
        if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
            return p


for a, b, c, d, e in pd([0, 1], repeat=5):
    matrix = [(1, 1, a, b),
              (1, 1, c, 1),
              (d, 1, 1, e)
              ]

    if len(matrix) == len(set(matrix)):
        print(*comb(), sep='')
        break
