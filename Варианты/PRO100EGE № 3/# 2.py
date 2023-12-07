from itertools import permutations as pm, product as pd


def f(x, y, z, w):
    return (not (x <= (not (z <= w)))) and (1-z <= (1-w == y))

for x in pd([0, 1], repeat=5):
    matrix = [(1, x[0], 1, 1),
              (x[1], x[2], 0, 0),
              (x[3], 0, 0, x[4])]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [0, 1, 1]:
                print(*p, sep='')
# xwzy
