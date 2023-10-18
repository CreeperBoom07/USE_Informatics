from itertools import product as pd

abc = sorted(set('РЕКУРСИЯ'))
k = 0
for ind, val in enumerate(pd(abc, repeat=6), start=1):
    if ind % 2 == 0:
        if val[0] != 'К' and sum(val.count(x) for x in 'ЕУИЯ') <= 2:
            k += 1
print(k)
            
# 9909
