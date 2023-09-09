from itertools import product as pd
k = 0
for x in pd('ВИШНЯ', repeat=6):
    if x.count('В') <= 1 and x[0] != 'Ш' and all(x[-1] != a for a in 'ИЯ'):
        k += 1
print(k)
# 4352
