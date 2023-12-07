def dif(n, m):
    return n % m == 0

def f(x):
    B = x in range(70, 81)
    return dif(x, 12) and B and 1-dif(x, a)


for a in range(1, 1000):
    if all(not f(x) for x in range(1, 100000)):
        print(a)
# 72
