from itertools import product as pd


def f(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    lst = list(d.values())

    if 3 in lst:
        lst.remove(3)
        for i in lst:
            if i > 1:
                return False
        return True
    else:
        return False


total = None
for ind, val in enumerate(pd(sorted('МАРКСЛ'), repeat=6), start=1):
    s = ''.join(val)
    if 'КС' not in s and 'СК' not in s and f(val):
        total = ind
print(total)

# 46605
