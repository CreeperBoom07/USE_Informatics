from itertools import combinations as comb


def f(x):
    P = 25 <= x <= 37
    Q = 32 <= x <= 50
    A = a1 <= x <= a2
    return (A and (not Q)) <= (P or Q)


Ox = [i/4 for i in range(20*4, 55*4)]

m = -1
for a1, a2 in comb(Ox, 2):
    if all(f(x) for x in Ox):
        # m.append(a2-a1)
        m = max(m, a2-a1)
print(m)

# 25
