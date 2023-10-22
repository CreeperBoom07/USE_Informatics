from itertools import product as pd

abc = sorted('ЛОГАРИФМ')
k = 0
for ind, val in enumerate(pd(abc, repeat=5), start=1):
    if ind % 2 == 0:
        s = ''.join(val)
        if (not s.startswith('ЛМ')) and s.count('И') >= 2:
            k += 1
print(k)
# 1288
