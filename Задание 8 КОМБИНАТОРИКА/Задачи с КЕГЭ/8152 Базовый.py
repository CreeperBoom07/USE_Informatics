from itertools import product as pd

for ind, val in enumerate(pd(sorted('ЛИНКОР'), repeat=4), start=1):
    s = ''.join(val)
    if s == 'КИНО':
        print(ind)
        break

# 239
