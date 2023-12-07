from fnmatch import *

def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return len(d)

for x in range(0, 10**9, 9162):
    if fnmatch(str(x), '*18??18'):
        print(x, f(x))
#2189718 24
#13184118 24
#84189618 40
#95184018 32
#166189518 96
