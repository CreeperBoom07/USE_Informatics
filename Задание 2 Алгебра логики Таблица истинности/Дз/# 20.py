from itertools import product as pd, permutations as pm


def f(x, y, z, w):
    return (x == 1-z) <= ((x or w) == y)

for x in pd([0, 1], repeat=5):
    matrix = [(0, x[0], 0, x[1]),
              (x[2], x[3], 0, 0),
              (x[4], 0, 0, 0)]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
                print(*p, sep='')
