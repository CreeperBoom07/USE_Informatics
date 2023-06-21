from itertools import product as pd
k = 1
for x in pd(sorted('МАРИЯ'), repeat=4):
    if k == 211:
        print(''.join(x))
        break
    k += 1