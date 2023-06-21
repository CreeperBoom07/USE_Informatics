from itertools import product as pd
k = 0

for x in pd('ДЕЙКСТРА', repeat=6):
    if len(x) == len(set(x)):
        if x.count('Й') == 1:
            if x[-1] != 'Й':
                if x[x.index('Й') + 1] in 'ДЙКСТР':
                    k += 1
print(k)
