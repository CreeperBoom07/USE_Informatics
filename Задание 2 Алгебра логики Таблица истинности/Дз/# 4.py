from itertools import product as pd, permutations as pm


def f(x, y, z, w):
    return ((1-x and y) == z) and w


for x in pd([0, 1], repeat=10):
    matrix = [(x[0], 0, x[1], x[2]),
              (x[3], x[4], x[5], 0),
              (0, 0, x[6], x[7]),
              (0, 0, x[8], x[9])
              ]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1, 1]:
                print(*p, sep='')

# yzwx
