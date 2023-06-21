from itertools import permutations as pm


def f(x, y, z):
    return not (x == (y <= z))


matrix = [(0, 0, 1),
          (0, 1, 1)]

for p in pm('xyz'):
    if [f(**dict(zip(p, row))) for row in matrix] == [1, 0]:
        print(*p, sep='')
