def f(x):
    A = ((x % a == 0) and (x % 24 == 0) and (x % 16 != 0))
    B = (x % a != 0)
    return A <= B


for a in range(1, 1000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break

# 16
