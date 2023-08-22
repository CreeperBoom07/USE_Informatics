from itertools import product as pd
k = 0
for ind, val in enumerate(pd(sorted('АКЛМНЯ'), repeat=5), start=1):
    s = ''.join(val)
    if s.startswith('МН'):
        k += 1
print(k-2)
# 214
