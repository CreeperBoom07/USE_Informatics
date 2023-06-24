def f(x, y):
    return (a > y) or (3*x + 2*y > 53) or (a > x)


for a in range(0, 1000):
    if all(f(x, y) for y in range(0, 100) for x in range(0, 100)):
        print(a)
        break


# 11
