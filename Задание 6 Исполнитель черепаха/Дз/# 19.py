from math import sqrt

k = 0
for x in range(-500, 500):
    for y in range(-500, 500):
        if y < x and y > -x and y < -x+55*sqrt(2) and y > x-55*sqrt(2):
            k += 1
print(k)
# 2965
