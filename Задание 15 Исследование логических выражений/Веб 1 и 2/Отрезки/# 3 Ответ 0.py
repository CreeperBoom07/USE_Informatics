from itertools import combinations as comb

def f(x):
    P = 1 <= x <= 98
    Q = 25 <= x <= 42
    A = a1 <= x <= a2
    return Q <= (((not P) and Q) <= A)


Ox = [i/4 for i in range(1*4, 100*4)]
m = 10**8
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, a2-a1)

print(m)

# 0.25 -> 0
