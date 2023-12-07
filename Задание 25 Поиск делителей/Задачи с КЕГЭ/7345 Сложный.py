from fnmatch import *
lst =[]
for x in range(0, 10**10, 4546):
    if fnmatch(str(x), '8*80*06'):
        lst += [[x, x//4546]]

for i in lst[::60]:
    print(*i)

# 81878006 18011
# 8185804906 1800661
# 8446518006 1858011
# 8780876306 1931561
# 8894980906 1956661