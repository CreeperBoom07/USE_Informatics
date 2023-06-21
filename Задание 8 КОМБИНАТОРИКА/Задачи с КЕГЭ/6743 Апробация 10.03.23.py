from itertools import product as pd
num = None
for ind, val in enumerate(pd(sorted('СОЙКА'), repeat=5), start=1):
    s = ''.join(val)
    if s.count('О') <= 1 and 'СС' not in s:
        num = ind
print(num)

# 2990
