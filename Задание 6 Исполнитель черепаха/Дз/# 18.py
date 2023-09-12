k = 0
for x in range(-200, 200):
    for y in range(-200, 200):
        if y < 3*x and y < 15 and y > (x-56)/4 and y > 0:
            k += 1
print(k)
