def div(n, m):
    return n % m == 0


def f(x):
    return (div(x, 2) <= 1-div(x, 3)) or (x+a >= 80)


for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break

# 74
