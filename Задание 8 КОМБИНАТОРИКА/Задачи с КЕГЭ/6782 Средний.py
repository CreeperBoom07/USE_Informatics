from itertools import product as pd

k = 0
lst = ['61', '16', '63', '36', '65', '56', '67', '76']
for x in pd('01234567', repeat=6):
    s = ''.join(x)
    if s[0] != '0' and s.count('6') == 2 and all(False if i in s else True for i in lst):
        k += 1

print(k)

# 5229
