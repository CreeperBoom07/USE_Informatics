def f(x, y):
    return (x + y <= 22) or (y <= x - 6) or (y >= a)


for a in range(1000):
    if all(f(x, y) for y in range(1, 150) for x in range(1, 150)):
        print(a)

# 9
