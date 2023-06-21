from itertools import permutations as pm


def f(a, b, c):
    return (a and 1-c) or (1-b and 1-c)


matrix = [(0, 0, 0),
          (0, 0, 1),
          (0, 1, 0),
          (0, 1, 1),
          (1, 0, 0),
          (1, 0, 1),
          (1, 1, 0),
          (1, 1, 1)]

for p in pm('abc'):
    if [f(**dict(zip(p, row))) for row in matrix] == [1, 0, 0, 0, 1, 0, 1, 0]:
        print(*p, sep='')

# abc
