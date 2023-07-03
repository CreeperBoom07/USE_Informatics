def div(n, m):
    return n % m == 0


def f(x):
    B = x in range(160, 181)
    return B <= (div(x, 35) <= div(x, a))


k = 0
for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        k += 1
print(k)

# 6
