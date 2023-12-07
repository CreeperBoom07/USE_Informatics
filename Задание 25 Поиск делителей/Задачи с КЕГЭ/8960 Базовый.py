from fnmatch import *

def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)


for x in range(500_001, 500_120):
    d = f(x)
    if fnmatch(str(sum(d)), '*7?'):
        print(x, sum(d))
#500001 666672
#500048 968874
#500069 500070
#500079 666776
#500114 750174
