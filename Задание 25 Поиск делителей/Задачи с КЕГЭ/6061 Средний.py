from fnmatch import *


def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x*0.5)+1))

def f(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d |= {i, x//i}
    return d


for x in range(0, 10**7):
    if fnmatch(str(x), '34?8*9'):
        d = [i for i in f(x) if p(i)]
        if len(d) > 4:
            print(x, max(d))

# 3408699 107
# 3418989 157
# 3428139 131
# 3428679 79
# 3438799 53
# 3468969 79
# 3488199 173
# 3488709 233
