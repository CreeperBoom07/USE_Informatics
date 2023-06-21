from itertools import product as pd
k = 0
for x in pd('01234567', repeat=4):
    num = ''.join(x)
    if int(num[0]) % 2 == 0 and num[0] != '0' and num[0] >= num[1] >= num[2] >= num[3]:
        k += 1
print(k)

