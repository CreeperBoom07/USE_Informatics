B = range(50, 71)


def f(x, y):
    return (2*x + y != 150) or (x not in B) or (a > y)


for a in range(0, 1000):
    if all(f(x, y) for y in range(100) for x in range(100)):
        print(a)
        break

# 51
