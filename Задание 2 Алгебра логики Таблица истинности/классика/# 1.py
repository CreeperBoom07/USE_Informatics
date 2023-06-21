from itertools import permutations as pm


def f(x, y, z):
    return ((not x) and y and z) or ((not x) and (not z))


matrix = [(0, 0, 0),
          (1, 0, 0),
          (1, 1, 0)
          ]

for p in pm('xyz'):
    if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
        print(*p, sep='')

# yzx
