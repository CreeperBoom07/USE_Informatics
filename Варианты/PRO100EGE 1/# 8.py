from itertools import product as pd
k = 0
for ind, val in enumerate(pd(sorted('КОМПЬЮТЕР'), repeat=5), start=1):
    if val[0] != 'Ь' and val.count('К') == 2 and ind % 2 != 0:
        k = ind
print(k)
# 58979
