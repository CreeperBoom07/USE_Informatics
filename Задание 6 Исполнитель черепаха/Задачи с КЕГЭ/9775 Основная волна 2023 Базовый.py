k = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        f1 = (0 <= x <= 20) and (0 <= y <= 13)
        f2 = (-3 <= x <= 5) and (8 <= y <= 24)
        if f1 or f2:
            k += 1
print(k)
# 441
