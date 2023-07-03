def f(x, y):
    return (7*y + x < a) or (2*x + 3*y > 98)


for a in range(0, 1000):
    if all(f(x, y) for y in range(1, 150) for x in range(1, 150)):
        print(a)
        break

# 226
