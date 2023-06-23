def f(x, y):
    return (x > 39) or (y > 26) or (2 * x + 4 * y < a)


for a in range(1, 1000):
    if all(f(x, y) for y in range(1, 100) for x in range(1, 100)):
        print(a)
        break

# 183
