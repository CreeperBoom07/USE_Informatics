def f(a, x):
    return (a % 9 == 0) and ((280 % x == 0) <= ((a % x != 0) <= (730 % x != 0)))


for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 10000)):
        print(a)
        break


# Второй вариант
for a in range(1, 1000):
    for x in range(1, 10000):
        if not f(a, x):
            break
    else:
        print(a)
        break
# 90
