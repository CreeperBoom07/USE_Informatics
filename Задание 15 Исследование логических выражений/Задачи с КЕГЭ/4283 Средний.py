from functools import reduce

P = {1, 3, 4, 9, 11, 13, 15, 17, 19, 21}
Q = set(range(3, 31, 3))
A = set()


def f(x):
    p = x in P
    a = x in A
    q = x in Q
    return (p <= a) or ((not a) <= (not q))


for x in range(1, 1000):
    if not f(x):
        A.add(x)

print(A)
print(reduce(lambda x, y: x*y, A, 1))


# 8505
