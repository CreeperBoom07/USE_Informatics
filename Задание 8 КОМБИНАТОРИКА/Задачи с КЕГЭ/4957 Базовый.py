from itertools import permutations as pm
k = 0

for x in set(pm('АНАСТАСИЯ')):
    s = ''.join(x)
    s = s.replace('И', 'А').replace('Я', 'А')
    for i in 'СТ':
        s = s.replace(i, 'Н')
    if 'ААА' not in s or 'ННН' not in s:
        k += 1

print(k)

# 23040
