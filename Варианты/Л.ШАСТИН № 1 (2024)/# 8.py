from itertools import product as pd

abc = sorted('ШКОЛА')

for ind, val in enumerate(pd(abc, repeat=5), start=1):
    if ''.join(val) == 'ШАЛАШ':
        print(ind)
        
# 2555
