from itertools import product as pd

for ind, val in enumerate(pd('АКЛМНЯ', repeat=5), start=1):
    s = ''.join(val)
    if s.startswith('КМ'):
        print(ind)
        break

# 1945
