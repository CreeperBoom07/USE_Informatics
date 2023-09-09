from itertools import product as pd

k = 0
for x in pd('ГЕПАРД', repeat=5):
    if x.count('Г') == 1 and x[0] != 'А' and x[-1] != 'Е':
        k += 1
print(k)
# 2200
