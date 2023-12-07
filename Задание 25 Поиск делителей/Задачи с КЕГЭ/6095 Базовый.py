from fnmatch import *
lst = []
for i in 111, 113, 127:
    for x in range(0, 10**8, i):
        if fnmatch(str(x), '*15*7424'):
            lst += [[x, x//i]]

for i in sorted(lst, key=lambda x: x[0]):
    print(*i)
# 1587424 14048
# 15147424 134048
# 15227424 137184
# 15457424 121712
# 28157424 221712
# 85157424 767184
