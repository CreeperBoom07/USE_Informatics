def f(x):
    return ((x&52 != 0) and (x&36 == 0)) <= (not (x&a == 0))

for a in range(1000):
    if all(f(x) for x in range(1000000)):
        print(a)
        break
# 16
