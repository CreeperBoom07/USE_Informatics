from itertools import combinations as comb


def div(n, m):
    return n % m == 0


def f(x):
    B = x in range(20, 81)
    A = a1 <= x <= a2
    return B <= (div(x, 17) <= A)


Ox = [i/4 for i in range(20*4, 81*4)]
m = 1000000
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, a2-a1)

print(m)

# 34
