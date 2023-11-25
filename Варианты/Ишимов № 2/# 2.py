from itertools import product as pd, permutations as pm

def f(x, y, z, w):
    return (1-x <= 1-y) and (not (w <= (x == z)) )

for x in pd([0, 1], repeat=5):
    matrix = [(x[0], x[1], x[2], 1),
              (1, x[2], 0, 0),
              (1, 0, 0, x[4])]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
                print(*p, sep='')
# wzyx
print(int('011', 2))
print(int('111', 2))
print(int('100', 2))
