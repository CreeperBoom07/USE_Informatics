from itertools import product as pd, permutations as pm

def f(x, y, z, w):
    return (x <= y) and z and 1-w

for x in pd([0, 1], repeat=4):
    matrix = [(0, 1, x[0], 1),
              (x[1], 1, x[2], x[3]),
              (0, 1, 1, 1)
              ]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
                print(*p, sep='')
# wzxy
