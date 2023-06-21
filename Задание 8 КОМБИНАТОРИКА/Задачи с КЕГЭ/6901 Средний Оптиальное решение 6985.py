from itertools import product as pd

total = None
for ind, val in enumerate(pd('АБРШ', repeat=5), start=1):
    s = ''.join(val)
    s = s.replace('Р', 'Б').replace('Ш', 'Б')
    if s.count('Б') <= 3:
        if len(set(val)) == 4 and any(val.count(i) == 2 for i in val):
            total = ind

print(total)

# 913
