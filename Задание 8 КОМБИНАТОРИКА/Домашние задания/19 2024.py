from itertools import product as pd

k = 0
for ind, val in enumerate(pd(sorted('АЛГОРИТМ'), repeat=4), start=1):
    s = ''.join(val)
    if s.endswith('ИМ'):
        k = ind
print(k)
# 4053
