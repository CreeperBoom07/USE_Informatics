from itertools import product as pd

comb = [''.join(i) for i in pd('01', repeat=16)]
P = {i for i in comb if i.startswith('01')}
Q = {i for i in comb if i[-1] == '1'}
A = set()


def f(x):
    q = x in Q
    p = x in P
    a = x in A
    return q <= (p and a)


for x in comb:
    if not f(x):
        A.add(x)

print(len(A))

# 32768
