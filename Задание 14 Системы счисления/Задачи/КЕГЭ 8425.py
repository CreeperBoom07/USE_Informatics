f = True
for p in range(2, 1000):
    if not f:
        break
    for x in range(1, p):
        if not f:
            break
        for y in range(0, p):
            if ((3*p + 2) * (1*p + 4)) == (x*p**2 + y*p + 2) and y!= 0:
                print(y*p + x)
                f = False
                break

# 23