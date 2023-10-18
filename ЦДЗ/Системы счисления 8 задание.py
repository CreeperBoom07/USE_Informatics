from itertools import product as pd

for ind, val in enumerate(pd('АКРУ', repeat=5), start=1):
    if ind == 350:
        print(''.join(val))
        break
