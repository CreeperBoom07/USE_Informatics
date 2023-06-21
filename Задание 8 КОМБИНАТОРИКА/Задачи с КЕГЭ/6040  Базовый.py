from itertools import product as pd
k = 0

for x in pd('0123456', repeat=6):
    if x[0] != '0' and x.count('6') == 1:
        s = ''.join(x)
        s = s.replace('2', '0').replace('4', '0').replace('6', '0')
        s = s.replace('3', '1').replace('5', '1')
        if '00' not in s and '11' not in s:
            k += 1

print(k)

# 1296
