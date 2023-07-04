def f(x, y, z):
    return (150 != y + 2 * x + 2 * z) or (a < x) or (a < y) or (a < z)


for a in range(0, 1000):
    if all(f(x, y, z) for z in range(1, 150) for y in range(1, 150) for x in range(1, 150)):
        print(a)

# 29
