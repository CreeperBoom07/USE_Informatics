from itertools import product as pd, permutations as pm


def f(a, b, c, d):
    return (1-a and 1-b) or (b == c) or d


for x in pd([0, 1], repeat=4):
    matrix = [(x[0], x[1], 1, x[2]),
              (1, 0, x[3], 1),
              (0, 0, 1, 1)]
    if len(matrix) == len(set(matrix)):
        for p in pm('abcd'):
            if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
                print(*p, sep='')
