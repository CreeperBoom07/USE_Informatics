from itertools import permutations as pm

def f(x, y, z):
    return (x or y) and (1-x or y or 1-z)

matrix = [(0, 0, 0),
          (0, 0, 1),
          (0, 1, 0),
          (0, 1, 1),
          (1, 0, 0),
          (1, 0, 1),
          (1, 1, 0),
          (1, 1, 1)]
for p in pm('xyz'):
    if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 1, 0, 1, 1, 1, 1]:
        print(*p, sep='')
# yxz
