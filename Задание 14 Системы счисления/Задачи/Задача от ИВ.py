def generator_loops():
    for p in range(8, 100):
        for x in range(0, p):
            for y in range(0, p):
                yield p, x, y


for p, x, y in generator_loops():
    n1 = 7*p + 1
    n2 = 5*p + 7
    n3 = x*p**2 + y*p + 7
    if n1*n2 == n3:
        print(y*p + x)
        break
