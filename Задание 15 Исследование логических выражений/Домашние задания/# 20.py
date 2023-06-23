from itertools import combinations as comb


def f(x):
    B = 18 <= x <= 52
    C = 16 <= x <= 41
    A = a1 <= x <= a2

    return (B <= A) and ((not C) or A)


Ox = [i / 4 for i in range(15 * 4, 55 * 4)]
m = 100000
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, a2 - a1)

print(m)

# 36
