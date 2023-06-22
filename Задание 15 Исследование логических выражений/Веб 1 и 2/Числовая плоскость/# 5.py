def f(x, y):
    return not (((x > 6) and ((x + y) >= 5)) or (y >= 5))


k = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        if f(x, y):
            k += 1
print(k)

# 35
