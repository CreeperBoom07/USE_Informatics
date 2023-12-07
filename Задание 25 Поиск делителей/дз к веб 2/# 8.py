from fnmatch import *

def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

for x in range(0, 10000000):
    if fnmatch(str(x), '?6*6*?6') and all(x%i==0 for i in [6, 7, 8]):
        print(x, sum(f(x)))
        
