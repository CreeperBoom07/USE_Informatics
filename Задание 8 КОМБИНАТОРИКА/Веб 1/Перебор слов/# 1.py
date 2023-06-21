from itertools import product as pd
k = 1
for x in pd('АКРУ', repeat=5):
    print(k, ''.join(x))
    if k == 150:
        break
    else:
        k+= 1
