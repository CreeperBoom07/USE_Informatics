from itertools import product as pd


for ind, val in enumerate(pd(sorted('ЛЕМУР'), repeat=4), start=1):
    if val[0] == 'Л':
        print(ind)
        break
# 126
