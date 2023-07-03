def div(n, m):
    return n % m == 0


def sumbol(s, d):
    return s + d > 0


def f(x):
    return (x + a >= 160) or (div(x, 7) <= (not sumbol(x, -17)))


for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break

# 139
