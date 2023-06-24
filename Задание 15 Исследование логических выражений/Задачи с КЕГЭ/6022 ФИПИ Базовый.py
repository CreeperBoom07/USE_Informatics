def f(x, y):
    return (x < a) or (y < a) or (x + 2*y > 150)


for a in range(0, 1000):
    if all(f(x, y) for y in range(0, 100) for x in range(0, 100)):
        print(a)
        break

# 51
