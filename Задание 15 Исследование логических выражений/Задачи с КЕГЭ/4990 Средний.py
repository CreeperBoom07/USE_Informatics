from itertools import combinations as comb

def div(n, m):
    return n % m == 0


def f(x):
    B = x in range(10, 41)
    A = a1 <= x <= a2
    return A or (B <= 1-div(x, 6))


Ox = [i/4 for i in range(10*4, 41*4)]
m = 100000
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, a2-a1)

print(m)

# 24
