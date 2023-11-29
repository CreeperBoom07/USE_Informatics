from fnmatch import *

def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return sorted(d)

for x in range(10**7, int(10**6.9), -1):
    if fnmatch(str(x), '9?*55*7'):
        d = sum(f(x))
        print(x, d%21)
#9995597 18
#9996557 12
#9997557 12
#9998557 17
#9999557 0



