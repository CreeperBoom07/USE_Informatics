from itertools import product as pd, \
    permutations as pm


def f(x, y, z, w):
    return ((y <= x) or ((not z) and w)) == (w == x)


# repeat=3 - количество пустот

for a in pd([0, 1], repeat=3):
    matrix = [(a[0], 1, 0, 0),
              (0, 0, 0, 1),
              (0, 1, a[1], a[2])
              ]
    # По условию строки в таблице не должны повторяться
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [1, 1, 1]:
                print(*p, sep='')
                break

# xwyz
