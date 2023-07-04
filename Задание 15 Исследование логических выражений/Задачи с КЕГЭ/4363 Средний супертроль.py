from itertools import combinations as comb


def f(x):
    A = 30 <= x <= 50
    P = 10 <= x <= 80
    Q = q1 <= x <= q2
    return Q <= (A and (not P))


Ox = [i/4 for i in range(5*4, 81*4)]
m = 10000000

for q1, q2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        m = min(m, q2-q1)
print(m)

q1 = 0
q2 = 0
if all(f(x) for x in Ox):
    print(q1-q2)

# 0
