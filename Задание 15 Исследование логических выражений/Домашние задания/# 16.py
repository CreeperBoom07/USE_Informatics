def f(x):
    p = x in P
    q = x in Q
    a = x in A
    return (a <= p) and (q <= (not a))


P = set(range(2, 21, 2))
Q = set(range(5, 51, 5))
A = set(range(1, 1000))

for x in range(1, 1000):
    if not f(x):
        A.remove(x)

# print(A)
print(len(A))

# 8
