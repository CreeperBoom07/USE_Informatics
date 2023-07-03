def div(n, m):
    return n % m == 0


def f(x, y):
    return (div(108, x) <= 1 - div(x, y)) or (x + y > 80) or (a - y > x)


for a in range(1, 1000):
    if all(f(x, y) for y in range(1, 1000) for x in range(1, 1000)):
        print(a)
        break

# 73
