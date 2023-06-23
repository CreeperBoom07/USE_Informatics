def f(x):
    a = x in A
    p = x in P
    q = x in Q
    return (p <= (not q)) or a


P = set(range(1, 12, 2))
Q = set(range(3, 13, 3))
A = set()

for x in range(1, 1000):
    if not f(x):
        A.add(x)

print(sum(A))

# 12
