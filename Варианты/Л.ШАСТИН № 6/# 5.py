for n in range(1, 1000):
    R = bin(n)[2:]
    if n % 5 == 0:
        R = R + R[-3:]
    else:
        R = R + bin((n%5)*5)[2:]
    if int(R, 2) > 256:
        print(n)
