from itertools import permutations as pm

k = 0
for x in pm('ЛЕВИОСА'):
    if all(False if x[0] == i else True for i in 'ЕИОА') and all(False if x[3] == i else True for i in 'ЛВС'):
        k += 1
print(k)

# 1440
