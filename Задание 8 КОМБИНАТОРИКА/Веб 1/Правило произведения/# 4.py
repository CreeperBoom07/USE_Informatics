from itertools import product
k = 0
for x in product('ЭЮЯ', 'АБВГ', 'АБВГ', 'АБВГ', 'ЭЮЯ'):
    k += 1
print(k)