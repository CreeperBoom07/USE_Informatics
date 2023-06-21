from itertools import permutations as pm


def f(a, b, c, d):
    return ((a and b) == 1-c) and (b <= d)


matrix = [(1, 0, 0, 0),
          (1, 0, 1, 0),
          (1, 0, 1, 1),
          (1, 1, 0, 0)]

for p in pm('abcd'):
    if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1, 1]:
        print(*p, sep='')
