from fnmatch import *

for x in range(0, 10**10, 50_068):
    s = str(x)
    if fnmatch(s, '9?979*8') and '0' in s:
        print(x, x//50068)

# 9097906348 181711
# 9297928008 185706
