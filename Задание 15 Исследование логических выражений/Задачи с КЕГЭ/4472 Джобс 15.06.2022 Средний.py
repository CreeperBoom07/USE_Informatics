from itertools import combinations as comb

def f(x):
    P = 254 <= x <= 800
    Q = 410 <= x <= 823
    A = a1 <= x <= a2
    return (P and (not A)) <= Q


Ox = [i/4 for i in range(254*4, 823*4)]
m = 100000000
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, a2-a1)
print(m)

# 155.75 -> 156
