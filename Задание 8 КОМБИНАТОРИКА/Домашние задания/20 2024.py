from itertools import product as pd

for ind, val in enumerate(pd(sorted('МАРИЯ'), repeat=4), start=1):
    s = ''.join(val)
    if s == 'АРИЯ':
        print(ind)
        break
# 85
