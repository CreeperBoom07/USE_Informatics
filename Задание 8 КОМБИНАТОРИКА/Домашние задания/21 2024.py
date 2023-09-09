from itertools import product as pd

for ind, val in enumerate(pd(sorted('МАРИЯ'), repeat=4), start=1):
    if ind == 211:
        print(*val, sep='')
        break
