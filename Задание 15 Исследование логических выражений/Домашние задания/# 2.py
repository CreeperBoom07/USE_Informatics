def f(x):
    A = ((x % 84 != 0) or (x % 90 != 0))
    B = (x % a != 0)
    return A <= B


for a in range(1, 10000):
    if all(f(x) for x in range(1, 100000)):
        print(a)
        break

# 1260
