def poz(n, m):
    return (n - m) > 0


def f(x, y):
    return (not poz(x+y, 73)) or (not poz(37, x-y)) or poz(y, a)


for a in range(0, 1000):
    if all(f(x, y) for y in range(0, 500) for x in range(0, 500)):
        print(a)

# 18
