p = set(range(2, 21, 2))
q = set(range(5, 51, 5))

a = set(range(1, 10000))

def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (A <= P) and (Q <= 1-A)

for x in range(1, 10000):
    if not f(x):
        a.remove(x)
print(len(a))
# 8
