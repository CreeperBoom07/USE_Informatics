from itertools import product as pd, permutations as pm


def f(x, y, z, w):
    return 1-w and ((y or z) <= (1-x and y))


for x in pd([0, 1], repeat=8):
    matrix = [(x[0], x[1], x[2], 1),
              (x[3], x[4], 1, x[5]),
              (x[6], 1, 1, x[7])]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
                print(*p, sep='')