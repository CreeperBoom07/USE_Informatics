def div(n, m):
    return n % m == 0


def f(x):
    B = x in range(70, 81)
    return div(x, a) or (B <= 1-div(x, 18))


for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)

# 72
