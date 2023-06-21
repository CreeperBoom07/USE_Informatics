from itertools import product as pd

k = 0
for x in pd('ВАЙФУ', repeat=4):
    s = ''.join(x)
    if len(x) == len(set(x)) and x[0] != 'Й' and all([False if sub in s else True for sub in ('ВФ', 'ФВ')]):
        k += 1
print(k)
