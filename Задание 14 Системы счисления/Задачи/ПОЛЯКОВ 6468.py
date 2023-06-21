def generator_loops():
    for p in range(10, 1000):
        for x in range(1, p):
            for y in range(0, p):
                yield p, x, y


for p, x, y in generator_loops():
    n1 = 7*p + 1
    n2 = 6*p + 9
    n3 = x*p**2 + y*p + 9
    if n1 * n2 == n3:
        print(y*p + x)
        break

# 1143
