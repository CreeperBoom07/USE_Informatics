from itertools import permutations as pm


def f(x, y, z, w):
    return (x <= y) or not (w <= z)


matrix = [(1, 0, 0, 1),
          (0, 0, 0, 1),
          (1, 0, 1, 1)]

for p in pm('xyzw'):
    if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
        print(*p, sep='')
