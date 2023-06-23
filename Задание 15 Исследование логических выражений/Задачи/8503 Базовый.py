def f(x):
    return ((x & 52 != 0) and (x & 36 == 0)) <= (x & a != 0)


for a in range(0, 1000):
    if all(f(x) for x in range(0, 10000)):
        print(a)
        break

# 16
