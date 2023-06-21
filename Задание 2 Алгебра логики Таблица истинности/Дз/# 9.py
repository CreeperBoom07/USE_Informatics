from itertools import permutations as pm


def f(x, y, z, w):
    return (y <= x or z) and (z <= y)


matrix = [(1, 0, 0, 0),
          (1, 1, 0, 0),
          (1, 1, 0, 1),
          (0, 1, 1, 0)]


for p in pm('xyzw'):
    if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0, 0]:
        print(*p, sep='')