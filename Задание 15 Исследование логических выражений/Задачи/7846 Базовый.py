from itertools import combinations as comb


def f(x):
    P = 13 <= x <= 19
    Q = 17 <= x <= 23
    A = a1 <= x <= a2
    return (not ((not P) <= Q)) <= (A <= ((not Q) <= P))


Ox = [i // 4 for i in range(10 * 4, 25 * 4)]
m = - 1
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = max(m, a2 - a1)
print(m)

# 10
