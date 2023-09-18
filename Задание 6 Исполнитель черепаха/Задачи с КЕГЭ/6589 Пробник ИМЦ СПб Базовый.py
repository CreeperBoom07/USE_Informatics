from math import sqrt

k = 0

for x in range(-1, 100):
    for y in range(-1, 100):
        if x > 0 and y < -(sqrt(3)/3)*x+16 and y > (sqrt(3)/3)*x:
            k += 1
print(k)
