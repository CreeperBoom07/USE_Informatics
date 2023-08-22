def f(x):
    return (x & 29 == 0) or ((x&11 == 0) <= (not (x & a == 0)))

for a in range(100000):
    if all(f(x) for x in range(15, 31)):
        print(a)
        break
