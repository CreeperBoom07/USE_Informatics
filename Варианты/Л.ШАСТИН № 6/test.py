n = 4

R = bin(n)[2:]
if n % 5 == 0:
    R = R + R[-3:]
else:
    R = R + bin((n%5)*5)[2:]
print(int(R, 2))
