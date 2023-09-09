from itertools import product as pd
k = 0
for x in pd('ВАЙФУ', repeat=4):
    if x[0] != 'Й' and len(x) == len(set(x)):
        s = ''.join(x)
        if 'ВФ' not in s and 'ФВ' not in s:
            k += 1
print(k)
# 68
