def f(x):
    A = ((x % 4 != 3) or (x % 6 != 1))
    B = (x % 36 != a)
    return A <= B


for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break

# 7
