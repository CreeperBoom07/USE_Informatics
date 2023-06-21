def generator_loops():
    for p in range(10, 100):
        for x in range(1, p):
            for y in range(1, p):
                yield p, x, y


for p, x, y in generator_loops():
    n1 = x*p**3 + x*p**2 + x*p + 8
    n2 = 4*p**3 + 3*p**2 + x*p + 9
    n3 = y*p**3 + y*p**2 + 0*p + 4
    if n1 + n2 == n3:
        print(y*p**2 + y*p + x)
        break

# 1826
