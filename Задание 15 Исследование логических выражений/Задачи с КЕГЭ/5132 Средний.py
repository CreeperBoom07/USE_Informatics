def od(n, m):
    for i in range(min(n, m), 1, -1):
        if n % i == 0 and m % i == 0:
            return True
    return False


def f(x):
    return (od(x, 42) <= 1-od(x, 7)) or (x+a>=25)


for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break

# 18
