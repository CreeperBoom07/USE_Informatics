def div(n, m):
    return n % m == 0


def f(x, y, z):
    return (div(z, 115) or div(y, 78) or div(x, 51)) <= div(x, a)


for a in range(1, 1000):
    if all(f(x, y, z) for z in range(1, 100) for y in range(1, 100) for x in range(1, 100)):
        print(a)

# 1
