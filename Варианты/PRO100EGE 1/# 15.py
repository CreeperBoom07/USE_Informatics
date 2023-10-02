def polygon(n, m, k):
    return n < m + k and m < n + k and k < n + m

def f(x):
    return not ((polygon(x, 11, 18) == (not(max(x, 5) > 68))) and polygon(x, a, 5))

for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
# 64
