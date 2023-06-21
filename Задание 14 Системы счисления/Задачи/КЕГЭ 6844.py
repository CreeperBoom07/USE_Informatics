def generator_loops():
    for p in range(10, 100):
        for x in range(1, p):
            for y in range(1, p):
                yield p, x, y


for p, x, y in generator_loops():
    n1 = 5*p**3 + x*p**2 + 8*p + 3
    n2 = x*p**3 + 9*p**2 + x*p + 9
    n3 = y*p**3 + 2*p**2 + 0*p + y
    if n1 + n2 == n3:
        print(x*p**3 + y*p**2 + y*p + x)
        break

# 18990
