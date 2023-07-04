from itertools import combinations as comb


def f(x):
    P = 5 <= x <= 40
    Q = 41 <= x <= 54
    R = 6 <= x <= 53
    A = a1 <= x <= a2
    return ((not P) <= Q) and R and not A


Ox = [i/4 for i in range(3*4, 55*4)]

m =10**20

for a1, a2 in comb(Ox, 2):
    if all(not f(x) for x in Ox):
        m = min(m, a2-a1)
print(m)

# 47
