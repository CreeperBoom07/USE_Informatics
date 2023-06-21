from itertools import permutations as pm


def f(x, y, z):
    return (1-x and y and z) or (1-x and 1-y and z) or (1-x and 1-y and 1-z)


matrix = [(0, 0, 0),
          (1, 0, 0),
          (1, 0, 1)]

for p in pm('xyz'):
    if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
        print(*p, sep='')

# zxy
