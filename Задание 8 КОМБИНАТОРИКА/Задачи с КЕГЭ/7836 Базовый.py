from itertools import product as pd

for ind, val in enumerate(pd(sorted('ГРАНТ'), repeat=6), start=1):
    s = ''.join(val)
    if s == 'ГРАНАТ':
        print(ind)
        break

# 5055
