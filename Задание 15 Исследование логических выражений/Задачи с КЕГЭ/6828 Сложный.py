"""!!! Не оптимальное решение"""
from itertools import combinations as comb


def div(n, m):
    return n % m == 0


def f(x):
    P = 257 <= x <= 356
    Q = 5 <= x <= 600
    R = 59 <= x <= 228
    A = a1 <= x <= a2
    return (R <= A) or ((div(x, 3) <= P) <= (Q <= A))


Ox = [i/4 for i in range(2*4, 605*4)]
m = 1000000
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, a2-a1)

print(m)

# 168.75 -> 169
