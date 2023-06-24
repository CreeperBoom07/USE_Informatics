def f(x):
    return (x % a == 0) or ((x in range(50, 71)) <= (x % 16 != 0))


for a in range(1, 10000):
    if all(f(x) for x in range(1, 100000)):
        print(a)

# 64
