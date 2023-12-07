from fnmatch import *

def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return d

for x in range(10**6):
    if fnmatch(str(x), '?8*8*?8'):
        if all(x % i == 0 for i in [6, 7, 8]):
            print(x, sum(f(x)))
##38808 133380
##48888 152880
##185808 565440
##188328 576000
##288288 1100736
##384888 1152000
##388248 1109760
