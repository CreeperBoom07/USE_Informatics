from itertools import combinations as comb


def f(x):
    D = 17 <= x <= 58
    C = 29 <= x <= 80
    A = a1 <= x <= a2
    return D <= (((not C) and (not A)) <= (not D))


Ox = [i / 4 for i in range(15 * 4, 81 * 4)]
m = 10000000
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, a2 - a1)

print(m)

# 11.75 -> 12
