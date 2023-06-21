from itertools import product as pd
k = 0
for x in pd('АРБУЗ', repeat=6):
    if x.count('А') == 3:
        s = ''.join(x)
        if 'АА' in s and 'ААА' not in s:
            k += 1

print(k)

# 768
