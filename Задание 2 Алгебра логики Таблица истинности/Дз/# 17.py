from itertools import product as pd, permutations as pm


def f(a, b, c, d):
    return (1-a and 1-b) or (b == c) or d


for a, b, c, d in pd([0, 1], repeat=4):
    matrix = [(1, 0, a, b),
              (1, 1, c, d),
              (1, 1, 1, 0)]
    if len(matrix) == len(set(matrix)):
        for p in pm('abcd'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
                print(*p, sep='')
