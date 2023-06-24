def f(x):
    return ((x & 17 != 0) <= ((x & a != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) and (x & a != 0) and (x & 58 == 0))


for a in range(1, 1000):
    if all(not f(x) for x in range(1, 10000)):
        print(a)
        break

# 2
