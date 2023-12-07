from fnmatch import *

for x in range(0, 10**10, 2023):
    if fnmatch(str(x), '1?1?1?1*1') and sum(int(i) for i in str(x))==22:
        print(x)

# 19131511
# 1012141291
# 1319111311
# 1516111051

