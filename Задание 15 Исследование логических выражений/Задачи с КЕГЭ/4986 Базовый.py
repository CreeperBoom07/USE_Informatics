def div(n, m):
    return n % m == 0


def f(x):
    B = x in range(50, 71)
    return div(x, a) or (div(x, 23) <= 1-B)


for a in range(1, 10000):
    if all(f(x) for x in range(1, 100000)):
        print(a)

# 69
