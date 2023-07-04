from itertools import combinations as comb


def f(x):
    P = 25 <= x <= 240
    Q = 175 <= x <= 300
    R = 270 <= x <= 340
    A = a1 <= x <= a2
    return (Q <= P) or ((not A) <= R)


Ox = [i / 4 for i in range(20 * 4, 341 * 4)]
m = 10 ** 11
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, a2 - a1)

print(m)

# 30
