from itertools import product as pd
lst = []
for ind, val in enumerate(pd(sorted('КОМПЬЮТЕР'), repeat=5), start=1):
    if ind % 2 != 0 and val[0] != 'Ь' and val.count('К') == 2:
        lst.append(ind)
print(lst[-1])