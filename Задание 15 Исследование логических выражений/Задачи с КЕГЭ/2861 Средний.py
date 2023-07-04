from itertools import combinations as comb


def f(x):
    P = 69 <= x <= 91
    Q = 77 <= x <= 114
    A = a1 <= x <= a2
    return Q <= ((P == Q) or ((not P) <= A))


Ox = [i/4 for i in range(68*4, 115*4)]
m = 10**10
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, a2-a1)
print(m)


# 22.75 -> 23
