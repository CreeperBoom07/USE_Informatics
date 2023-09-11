k = 0
for x in range(0, 100):
    for y in range(0, 100):
        if y > 0 and y <(3**.5)*x and y < - (3**.5)*x+15*3**.5:
            k += 1
print(k)
# 90
