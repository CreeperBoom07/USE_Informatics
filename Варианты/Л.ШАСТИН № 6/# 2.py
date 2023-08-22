from itertools import permutations as pm

def f(x, y, z, w):
    return x and 1-y and (1-z or w)


matrix = [(0, 0, 1, 0),
          (0, 0, 1, 1),
          (1, 0, 1, 1)]

for p in pm('xyzw'):
    if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
        print(*p, sep='')
