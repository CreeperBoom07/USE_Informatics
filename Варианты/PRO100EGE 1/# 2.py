from itertools import product as pd, permutations as pm

def f(x, y, z, w):
    return (x or 1-y) and (not (x==z)) and w


for x in pd([0, 1], repeat=4):
    matrix = [(x[0], 0, 0, 1),
              (0, 0, 1, 1),
              (0, x[1], x[2], x[3])
              ]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
                print(*p, sep='')
# zyxw
