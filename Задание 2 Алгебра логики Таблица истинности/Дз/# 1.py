from itertools import product as pd, permutations as pm


def f(x, y, z, w):
    return (x or 1-y) and not (y == z) and w


for a, b, c, d in pd((0, 1), repeat=4):
    matrix = [(0, 1, a, 0),
              (b, 1, 1, 0),
              (1, c, 0, d)]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
                print(*p, sep='')

# xwzy
