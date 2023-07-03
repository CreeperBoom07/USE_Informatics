def f(x, y):
    return (not ((x + 5 < a) <= (y > a))) or (x*y >= 76)


for a in range(1, 1000):
    if all(f(x, y) for y in range(1, 100) for x in range(1, 100)):
        print(a)
        break

# 81
