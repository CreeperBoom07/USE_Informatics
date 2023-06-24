def f(x):
    A = ((x % 115 == 0) and (x % 5 != 0))
    B = (((a % x == 0) <= (a % 5 != 0)) and (a not in range(5, 138)))
    return A or B


for a in range(1, 1000):
    f1 = 0
    f2 = 0
    for x in range(1, 10000):
        if f(x):
            f1 += 1
        else:
            f2 += 1
    if f1 > 0 and f2 > 0:
        print(a)
        break

# 140
