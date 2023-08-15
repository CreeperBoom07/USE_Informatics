from itertools import product as pd, permutations as pm


def f(x, y, z, w):
    return w or (y <= z) and x


for x in pd([0, 1], repeat=6):
    matrix = [(x[0], x[1], 0, 0),
              (1, 1, x[2], x[3]),
              (1, x[4], x[5], 1)
              ]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1, 0, 0]:
                print(*p, sep='')

