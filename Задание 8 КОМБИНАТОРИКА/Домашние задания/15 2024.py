from itertools import product as pd

k = 0

for x in pd('ДЕЙКСТРА', repeat=6):
    if x.count('Й') == 1 and len(x) == len(set(x)):
        s = ''.join(x)
        if any('Й'+c in s for c in 'ДКСТР'):
            k += 1
print(k)
# 9000
        
