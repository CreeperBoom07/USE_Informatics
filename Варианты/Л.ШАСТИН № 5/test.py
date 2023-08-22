n = 12

R = bin(n)[2:]
if n % 5 == 0:
    R = R + R[-3:]
else:
    R = bin((n%5)*5)[2:] + R
print(int(R, 2))
