from itertools import product as pd

for ind, val in enumerate(pd('АВЛОР', repeat=4), start=1):
    if val[0] == 'Л':
        print(ind)
        break

# 251
