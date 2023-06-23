def f(x):
    A = ((x & 26 != 0) or (x & 13 != 0))
    B = ((x & 29 == 0) <= (x & a != 0))
    return A <= B


for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break

# 2
