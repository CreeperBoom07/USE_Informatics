from itertools import combinations as comb


def f(x):
    P = 17 <= x <= 54
    Q = 37 <= x <= 83
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))


Ox = [i / 4 for i in range(15 * 4, 85 * 4)]
m = 1000000
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, a2 - a1)

print(m)

# 17
