from itertools import product as pd, permutations as pm


def f(x, y, w, z):
    return 1 - (y <= (x==w)) and (z <= x)


for a, b, c, d, e in pd([0, 1], repeat=5):
    matrix = [(a, 1, 1, b),
              (0, c, d, 0),
              (e, 0, 1, 0)]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
                print(*p, sep='')


