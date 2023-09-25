def d(n, m):
    return n % m == 0

def f(x):
    return d(x, a) <= (1-d(x, 28) or d(x, 42))

for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break
