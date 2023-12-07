from fnmatch import *

def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))

lst = []
prost = [i for i in range(0, 10**5) if p(i)]
for i in range(len(prost)):
    if p(i+1):
        lst += [prost[i]]
for x in lst:
    if fnmatch(str(x), '1*7?7'):
        print(x, prost.index(x)+1)

# 1787 277
# 13757 1627
# 18757 2141
# 18787 2143
# 19777 2239