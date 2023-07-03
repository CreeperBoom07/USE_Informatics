from itertools import combinations as comb


def f(x):
    P = 35 <= x <= 55
    Q = 45 <= x <= 65
    A = a1 <= x <= a2
    return (P <= A) and ((not A) <= (not Q))


Ox = [i / 4 for i in range(35 * 4, 65 * 4)]
m = 1100000
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, a2 - a1)

print(m)

# 29.75 -> 30
