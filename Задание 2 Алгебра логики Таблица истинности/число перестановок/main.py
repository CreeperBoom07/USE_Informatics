from itertools import product as pd,\
    permutations as pm


def f(x, y, z, w):
    # print(x, '->', type(x), y, '->', type(y))
    return (y <= x) and 1-z and w


for x in pd([0, 1], repeat=6):
    matrix = [(1, 0, x[0], x[1]),
              (1, 1, x[2], x[3]),
              (x[4], 1, 1, x[5])]
    if len(matrix) == len(set(matrix)):

        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
                print(*p, sep='')
