from itertools import product as pd
combinations = [''.join(i) for i in pd('АВОРТ', repeat=6)]
for ind, val in enumerate(combinations, start=1):
    if val == 'ВОРОТА':
        print(ind)
        break

# 4821
