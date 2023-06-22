from itertools import combinations as comb

def f(x):
    P = 5 <= x <= 100
    Q = 15 <= x <= 25
    R = 35 <= x <= 50
    A = a1 <= x <= a2
    return (P <= Q) or ((not A) <= R)


Ox = [i/4 for i in range(1*4, 105*4)]
m = 10**8
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, a2-a1)
print(m)

# 95
