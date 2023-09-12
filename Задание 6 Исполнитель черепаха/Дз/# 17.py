k = 0
for x in range(-200, 200):
    for y in range(-200, 200):
        if y > x and y < 90 and y < 3*x:
            k += 1
print(k)
