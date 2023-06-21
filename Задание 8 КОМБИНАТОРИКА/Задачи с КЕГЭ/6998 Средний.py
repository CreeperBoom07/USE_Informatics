from itertools import product as pd

k = 0
for x in pd('QWERTYNO', repeat=7):
    s = ''.join(x)
    if 'QWERTY' not in s and all(False if s.count(i) > 2 else True for i in 'QWERTYNO'):
        k += 1
print(k)

# 1345664
