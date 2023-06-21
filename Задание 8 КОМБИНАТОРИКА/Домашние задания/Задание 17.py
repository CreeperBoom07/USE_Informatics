from itertools import product as pd
k = 1
for x in pd(sorted('ЛЕМУР'), repeat=4):
    if x[0] == 'Л':
        print(k)
        break
    else:
        k += 1