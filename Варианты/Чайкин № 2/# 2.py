from itertools import product as pd, permutations as pm

def f(x, y, z, w):
    return (x <= y) and (y <= z) and (z <= w)

for x in pd([0, 1], repeat=6):
    matrix = [(x[0], x[1], 1, 0),
              (x[2], 0, x[3], 1),
              (1, x[4], 0, x[5])
              ]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
                print(*p, sep='')
# wxzy
