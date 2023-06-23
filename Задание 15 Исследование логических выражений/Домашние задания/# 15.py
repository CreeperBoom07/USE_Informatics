def f(x):
    a = x in A
    p = x in P
    q = x in Q
    return (not ((not a) and p)) or (not q)


A = set()
P = set(range(3, 13, 3))
Q = set(range(1, 7))

for x in range(1, 1000):
    if not f(x):
        A.add(x)

# print(A)
print(len(A))

# 2
