from math import sqrt
k = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        if x >= 0 and x < 26 and y <= (sqrt(3)/3)*x + 15 and \
        y < -(sqrt(3)/3)*x + 41 and y > -(sqrt(3)/3)*x \
        and y > (sqrt(3)/3)*x - 26:
            k += 1
print(k)
