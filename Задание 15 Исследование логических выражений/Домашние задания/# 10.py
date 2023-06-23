def f(x, y):
    return (x*y > a) and (x > y) and (x < 8)


for a in range(0, 1000):
    if all(not f(x, y) for y in range(1, 100) for x in range(1, 100)):
        print(a)
        break

# 42
