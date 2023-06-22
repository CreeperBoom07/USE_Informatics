a = set(range(1, 1000))
p = set(range(2, 21, 2))
q = set(range(5, 51, 5))


def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (A <= P) and (Q <= (not A))


for x in range(1, 1000):
    if not f(x):
        a.remove(x)

print(a)
print(len(a))

# 8
