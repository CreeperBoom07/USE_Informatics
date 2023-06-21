from itertools import product as pd
k = 1
for x in pd(sorted('МАРИЯ'), repeat=4):
    s = ''.join(x)
    if s == 'АРИЯ':
        print(k)
        break
    else:
        k += 1

