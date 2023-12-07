from fnmatch import *

def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    l = len(d)
    while l != 2:
        l //= 2
        if l < 2:
            return False
    return True


for x in range(0, 10**9, 62961):
    if fnmatch(str(x), '*31*65?') and f(x):
        print(x, x//2031)

# 53831655 26505
# 333126651 164021
# 512313657 252247
# 647931651 319021
# 831966654 409634