from itertools import product as pd, permutations as pm


def f(x, y, z, w):
    return (x <= (z==w)) or (not (y <= w))


for x in pd((0, 1), repeat=7):
    matrix = [(x[0], 1, x[1], x[2]),
              (0, x[3], 0, x[4]),
              (x[5], 0, 0, x[6])]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
                print(*p, sep='')

