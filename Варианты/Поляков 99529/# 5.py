lst = []
for n in range(1, 1000):
    R = bin(n)[2:]
    if n % 5 == 0:
        R = '1' + R + R[-2:]
    else:
        R = bin(n%5)[2:] + R
    if int(R, 2) <= 223:
        lst.append(int(R, 2))
print(max(lst))
# 219
        
