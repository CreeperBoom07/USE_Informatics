def f(x):
    return ((x % 13 == 0) <= (x not in range(40, 61))) or (a < x + 20)


for a in range(1, 10000):
    if all(f(x) for x in range(1, 100000)):
        print(a)

# 71
