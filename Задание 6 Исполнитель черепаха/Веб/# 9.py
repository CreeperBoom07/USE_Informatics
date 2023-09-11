k = 0
for x in range(0, 300):
    for y in range(0, 400):
        if y > 0 and y < 2*x and y < -3*x+750:
            k += 1
print(k)
# 37251
