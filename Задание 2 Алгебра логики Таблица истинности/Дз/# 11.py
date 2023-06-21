from itertools import product as pd, permutations as pm


def f(x, y, z, w):
    return (y <= x) or (not ((x <= z) and (z <= x))) and 1-w


for x in pd([0, 1], repeat=6):
    matrix = [(0, 0, 0, x[0]),
              (x[1], 0, 0, x[2]),
              (x[3], x[4], 0, x[5])]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
                print(*p, sep='')

# wzxy
