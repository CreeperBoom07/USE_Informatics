f=True
for p in range(7, 20):
    for x in range(1, p):
        for y in range(1, p):
            n1 = y*p**2 + 4*p + y
            n2 = y*p**2 + 6*p + 5
            for z in range(0, p):
                n3 = x*p**3 + z*p**2 + 3*p + 3
                if n1 + n2 == n3:
                    print(x*p**2 + y*p + z)


# 117
