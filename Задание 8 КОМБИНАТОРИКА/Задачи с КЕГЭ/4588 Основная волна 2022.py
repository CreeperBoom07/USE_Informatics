from itertools import product as pd

k = 0
for x in pd('01234567', repeat=5):
    if x[0] != '0' and x.count('6') == 1:
        s = ''.join(x)
        for i in '357':
            s = s.replace(i, '1')
        if '61' not in s and '16' not in s:
            k += 1
print(k)

# 2961
