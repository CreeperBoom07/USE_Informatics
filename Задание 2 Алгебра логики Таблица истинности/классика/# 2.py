from itertools import permutations as pm


def f(x, y, z, w):
    return (not y) or x or ((not z) and w)


matrix = [(0, 0, 0, 1),
          (0, 0, 1, 1),
          (1, 0, 1, 1)
          ]


for p in pm('xywz'):
    if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
        print(*p, sep='')

# wxzy
