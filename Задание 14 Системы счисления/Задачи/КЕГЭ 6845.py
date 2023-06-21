def loops_generator():
    for p in range(8, 100):
        for x in range(1, p):
            for y in range(1, p):
                yield p, x, y


for p, x, y in loops_generator():
    n1 = 1*p**3 + x*p**2 + 7*p + 7
    n2 = x*p**3 + x*p**2 + 7*p + 7
    n3 = y*p**3 + 0*p**2 + y*p + y
    if n1 + n2 == n3:
        print(y*p**3 + x*p**2 + y*p + x)
        break

# 200796
