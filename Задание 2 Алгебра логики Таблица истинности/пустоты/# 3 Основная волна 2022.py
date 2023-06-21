from itertools import product as pd, \
    permutations as pm

'''Лайфхак!!! Вместо not можно писать 1-<лог.переменная>'''
def f(x, y, z, w):
    return ((x <= z) <= y) or 1-w


for lst in pd([0, 1], repeat=7):

    matrix = [(1, 0, lst[0], lst[1]),
              (lst[2], 1, 0, lst[3]),
              (0, lst[4], lst[5], lst[6])
              ]

    if len(matrix) == len(set(matrix)):
        for p in pm('xyzw'):
            if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
                print(*p, sep='')

# zxyw
