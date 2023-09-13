k = 0
for x in range(0, 50):
    for y in range(0, 50):
        f1 = (0 <= y <= 8) and (0 <= x <= 18)
        f2 = (4 <= y <= 21) and (10 <= x <= 17)
        if f1 or f2:
            k += 1
print(k)
# 275
