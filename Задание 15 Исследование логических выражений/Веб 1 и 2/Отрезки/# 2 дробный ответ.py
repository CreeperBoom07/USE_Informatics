from itertools import combinations as comb

"""Если в ответе дробное число, то его надо округлить!!!"""


def f(x):
    P = 2 <= x <= 20
    Q = 15 <= x <= 25
    A = a1 <= x <= a2
    return ((not A) <= (not P)) or Q


Ox = [i / 4 for i in range(1 * 4, 30 * 4)]
m = 10 ** 8
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, a2 - a1)

print(m)

# 12.75 -> 13
