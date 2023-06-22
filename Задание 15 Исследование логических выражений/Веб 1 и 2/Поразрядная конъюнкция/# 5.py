def f(a, x):
    return ((x & 17 != 0) <= ((x & a != 0) <= (x & 58 != 0))) <= ((x & 8 == 0) and (x & a != 0) and (x & 58 == 0))


for a in range(43, 56):
    if all(not f(a, x) for x in range(1, 1000000)):
        print(a)


# 50
