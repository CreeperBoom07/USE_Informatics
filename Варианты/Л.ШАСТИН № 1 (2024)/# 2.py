from itertools import product as pd, permutations as pm

def f(x, y, z, w):
    return (x <= y) and (1-y <= z) and w

for x in pd([0, 1], repeat=6):
    matrix = [(x[0], x[1], 0, 0),
              (0, 1, 0, x[2]),
              (0, x[3], x[4], x[5])]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1 , 1, 1]:
                print(*p, sep='')
# zwxy
