for n in range(11, 1000):
    R = bin(n)[2:]
    if n % 5 == 0:
        R = R + R[-3:]
    else:
        R = bin((n%5)*5)[2:] + R
    if int(R, 2) > 512:
        print(n)
        break
