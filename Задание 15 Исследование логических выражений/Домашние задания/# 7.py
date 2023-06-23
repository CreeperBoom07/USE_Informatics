def f(x):
    A = (((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0))
    B = ((x & a != 0) and (x & 39 == 0))
    return A or B


for a in range(1, 10000):
    if all(f(x) for x in range(1, 100000)):
        print(a)

# 13
