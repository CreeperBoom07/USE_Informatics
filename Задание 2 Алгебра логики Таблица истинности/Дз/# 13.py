from itertools import product as pd, permutations as pm


def f(x, y, w, z):
    return ((w <= y) or (not (y <= z))) and 1 - x and (not (x == z))


for x in pd([0, 1], repeat=5):
    matrix = [(0, x[0], 1, x[1]),
              (1, x[2], x[3], 1),
              (0, x[4], 1, 1)]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
                print(*p, sep='')
