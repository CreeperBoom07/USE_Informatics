from itertools import product as pd, permutations as pm

def f(x, y, z, w):
    return (x and 1-y) or (x==z) or w

for a, b, c, d in pd([0, 1], repeat=4):
    matrix = [(1, a, 0, 0),
              (1, 1, b, 0),
              (c, 1, 1, d)]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
                print(*p, sep='')
# zyxw
