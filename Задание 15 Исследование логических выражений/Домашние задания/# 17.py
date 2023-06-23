from functools import reduce


def f(x):
    a = x in A
    p = x in P
    q = x in Q
    r = x in R
    return (not a) <= ((p and q) <= r)


P = set(range(2, 21, 2))
Q = set(range(3, 31, 3))
R = set(range(12, 61, 12))
A = set()


for x in range(1, 1000):
    if not f(x):
        A.add(x)

# print(A)
print(reduce(lambda x, y: x*y, A))

# 108
