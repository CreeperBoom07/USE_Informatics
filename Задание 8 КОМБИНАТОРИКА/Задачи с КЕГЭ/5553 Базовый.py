from itertools import permutations as pm
k = 0
for x in set(pm('СОТОЧКА')):
    s = ''.join(x)
    s = s.replace('А', 'О')
    if 'ОО' in s:
        k += 1
print(k)

# 1800
