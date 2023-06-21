from itertools import product as pd

lst = []
for ind, val in enumerate(pd(sorted('КОФЕ'), repeat=5), start=1):
    if val.count('О') == 1:
        s = ''.join(val)
        if all(False if i in s else True for i in ['КО', 'ОК', 'ОФ', 'ФО']):
            lst.append(ind)

print(lst[0]+lst[-1])

# 1014
