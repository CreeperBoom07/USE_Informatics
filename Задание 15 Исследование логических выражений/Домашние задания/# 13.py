def f(x, y):
    return (x**2 - 10*x + 16 > 0) or (y**2 - 10*y + 21 > 0) or (x*y < 2*a)

for a in range(0, 1000):
    if all(f(x, y) for y in range(1, 100) for x in range(1, 100)):
        print(a)
        break

# 29
