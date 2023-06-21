from itertools import product as pd,\
    permutations as pm


def f(x, y, z, w):
    return x and (y <= z) or w


s = set()  # Используем set, т.к. таблицы могут повторяться
for a, b, c, d, e, g in pd([0, 1], repeat=6):
    matrix = [(1, 0, a, 1),
              (b, 0, 1, c),
              (d, 0, e, g)
              ]
    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
                s.add(p)

print(len(s))
