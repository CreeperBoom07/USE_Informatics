k = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        if y < -x and y > -x-10*(2**.5) and y < x+10*(2**.5) and y > x-10*(2**.5):
            k += 1
print(k)
# 203
