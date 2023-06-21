from itertools import *

def f(p1, p2, p3, p4):
    return (p3 <= p1) <= (p4 or 1 - p2)


for a, b, c, d in product([0, 1], repeat=4):
    matrix = [(0, 0, a, 1),
              (0, 1, b, 1),
              (1, 1, c, d)]
    if len(matrix) == len(set(matrix)):
        for p in permutations(['p1', 'p2', 'p3', 'p4']):
            if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
                print(p)

# ('p3', 'p1', 'p4', 'p2')
#   x     y     z     w
# ywxz
