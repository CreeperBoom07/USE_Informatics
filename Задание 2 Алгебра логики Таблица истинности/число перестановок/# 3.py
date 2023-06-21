from itertools import permutations

def f(x, y, z, w):
    return (y or x) == ((y <= w) or 1-z)


matrix = [(1, 0, 0, 0),
          (0, 1, 0, 0),
          (1, 0, 1, 0)
          ]

for p in permutations('xyzw'):
    if [f(**dict(zip(p, row))) for row in matrix] == [0, 0, 0]:
        print(p)