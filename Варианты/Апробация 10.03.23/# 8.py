from itertools import product as pd
k = 0
for ind, val in enumerate(pd(sorted('СОЙКА'), repeat=5), start=1):
    if val.count('О') <= 1:
        s = ''.join(val)
        if 'СС' not in s:
            k = ind
print(k)
