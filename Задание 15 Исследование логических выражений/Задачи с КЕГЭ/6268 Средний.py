from itertools import combinations as comb


def f(x):
    B = 23 <= x <= 37
    C = 41 <= x <= 73
    A = a1 <= x <= a2
    return not (((not B) <= C) <= A)


Ox = [i / 4 for i in range(20*4, 75*4)]
m = 100000
for a1, a2 in comb(Ox, 2):
    if all(not f(x) for x in Ox):
        m = min(m, a2-a1)

print(m)

# 50
