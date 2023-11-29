from fnmatch import *

def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

for x in range(0, 10**7, 217):
    if fnmatch(str(x), '14?4*'):
        print(x, sum(i for i in f(x) if i % 2 != 0))
#1484714 958464
#1484931 2336768
#1494045 3345408
#1494262 964608
#1494479 1806336
#1494696 306432
#1494913 1785088
