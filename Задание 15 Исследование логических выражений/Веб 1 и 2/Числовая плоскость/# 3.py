def f(a, x, y):
    return (2*y + 3*x < a) or (x + y > 40)


for a in range(1, 1000):
    if all(f(a, x, y) for y in range(100) for x in range(100)):
        print(a)
        break

# 121
