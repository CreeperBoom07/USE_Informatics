def f(x, y):
    return (x > a) or (y > a) or (y - 2*x + 12 != 0)


for a in range(0, 1000):
    if all(f(x, y) for y in range(0, 150) for x in range(0, 150)):
        print(a)

# 5
