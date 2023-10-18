def dif(n, m):
    return n % m == 0

def f(x):
    return 1 - dif(x, a) or 1- (dif(x, 12) and dif(x, 23))

for a in range(1, 1000):
    if all(f(x) for x in range(1, 100000)):
        print(a)
        break
# 365
