def polygon(n, m, k):
    return n + m > k and n + k > m and m + k > n


def f(x):
    return polygon(a, 5, x) <= ((max(x, 11) <= 19) == (not polygon(23, 13, x)))


for a in range(1, 10000):
    if all(f(x) for x in range(1, 100000)):
        print(a)

# 31

