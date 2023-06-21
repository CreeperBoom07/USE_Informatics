from itertools import *


def f(x, y, z, w):
    return (x and 1 - y) or (x == z) or w

for x in product([0, 1], repeat=6):
    matrix = [(1, x[0], x[1], 1),
              (x[2], 0, x[3], 0),
              (1, x[4], 1, x[5])]
    if len(matrix) == len(set(matrix)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
                print(*p, sep='')
