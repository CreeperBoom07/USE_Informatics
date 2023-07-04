def div(n, m):
    return n % m == 0


def f(x):
    return (div(x, 3) <= 1-div(x, 5)) or (x+a >= 70)


for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break

# 55
