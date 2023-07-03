def div(n, m):
    return n % m == 0


def f(x):
    return (div(x, 3) <= (not div(x, 17))) or not (a < 190 - x)


for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break

# 139
