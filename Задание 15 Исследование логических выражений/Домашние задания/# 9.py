from itertools import product as pd


def f(x):
    return (x not in A) <= ((x in P) or (x not in Q))


comb = [''.join(i) for i in pd('01', repeat=8)]
P = {i for i in comb if i.startswith('11')}
Q = {i for i in comb if i[-1] == '0'}
A = set()

for x in comb:
    if not f(x):
        A.add(x)


print(len(A))

# 96
