from itertools import product as pd
r = 0
l = 0
for ind, val in enumerate(pd(sorted('АЗНС'), repeat=5), start=1):
    s = ''.join(val)
    if s == 'САЗАН':
        l = ind
    if s == 'ЗАНАС':
        r = ind
print(l-r+1)
# 496
