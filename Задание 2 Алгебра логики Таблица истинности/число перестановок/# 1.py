from itertools import permutations as pm


def f(x, y, z, w):
    return (x == y) <= (z == w)


matrix = [(0, 0, 0, 1),
          (1, 1, 1, 0)]
k = 0
for p in pm('xyzw'):
    if [f(**dict(zip(p, row))) for row in matrix] == [0, 0]:
        k += 1
print(k)

# 12
